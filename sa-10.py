#!/usr/bin/env python3
from argparse import ArgumentParser, BooleanOptionalAction
from pathlib import Path
from subprocess import call
from time import time

from diffusers import StableAudioPipeline
from ffmpeg import FFmpeg
from slugify import slugify
from soundfile import write as write_soundfile
from torch import bfloat16


def main(arguments):
    model = arguments.model
    prompt = arguments.prompt
    length = arguments.length
    inference_steps = arguments.inference_steps
    samples_per_batch = arguments.samples_per_batch
    open_outputs = arguments.open_outputs

    prompt = [prompt] * samples_per_batch

    negative_attributes = (
        "low quality",
        "low fidelity",
        "annoying",
    )
    negative_prompt = [", ".join(negative_attributes)] * samples_per_batch

    datatype = bfloat16

    pipeline = StableAudioPipeline.from_pretrained(model, torch_dtype=datatype)
    pipeline.to("cuda")

    audios = pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=inference_steps,
        audio_end_in_s=length,
    ).audios

    slugified_prompt = slugify(prompt[0])
    slugified_model_name = slugify(model)
    for audio in audios:
        output = audio.T.float().cpu().numpy()
        wav_extension = "wav"
        try:
            filename_base = f"outputs/{time()}-{slugified_model_name}-{length}s-{slugified_prompt}"
            filename = f"{filename_base}.{wav_extension}"
            write_soundfile(
                filename,
                output,
                pipeline.vae.sampling_rate,
            )
        except OSError:
            filename_base = f"outputs/{time()}-{slugified_model_name}-{slugified_prompt}s.wav"
            filename = f"{filename_base}.{wav_extension}"
            write_soundfile(
                filename,
                output,
                pipeline.vae.sampling_rate,
            )

        m4a_extension = "m4a"
        ffmpeg = FFmpeg().input(filename).output(f"{filename_base}.{m4a_extension}")
        ffmpeg.execute()
        path_to_unlink = Path(filename)
        path_to_unlink.unlink()

    if open_outputs:
        call(("open", "outputs"))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--model", default="stabilityai/stable-audio-open-1.0", required=False)
    parser.add_argument("--prompt", default="hammered dulcimer solo", required=False)
    parser.add_argument("--length", default=30, type=int, required=False)
    parser.add_argument("--inference-steps", default=256, type=int, required=False)
    parser.add_argument("--samples-per-batch", default=1, type=int, required=False)
    parser.add_argument("--open-outputs", default=True, action=BooleanOptionalAction, required=False)

    arguments = parser.parse_args()

    main(arguments)
