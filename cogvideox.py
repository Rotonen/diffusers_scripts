#!/usr/bin/env python3
from argparse import ArgumentParser
from subprocess import call
from time import time

from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_gif
from slugify import slugify
from torch import bfloat16


def main(model, prompt, resolution, inference_steps, videos_per_batch):
    width, height = resolution

    prompt = [prompt] * videos_per_batch

    datatype = bfloat16

    pipeline = CogVideoXPipeline.from_pretrained(model, torch_dtype=datatype)
    pipeline.enable_model_cpu_offload()
    pipeline.to(datatype)

    videos = pipeline(
        prompt=prompt,
        guidance_scale=6,
        num_inference_steps=inference_steps,
        width=width,
        height=height,
    ).frames

    slugified_prompt = slugify(prompt[0])
    slugified_model_name = slugify(model)
    for video in videos:
        try:
            export_to_gif(video, f"outputs/{time()}-{slugified_model_name}-{width}-{height}-{slugified_prompt}.gif")
        except OSError:
            export_to_gif(video, f"outputs/{time()}-{slugified_model_name}-{width}-{height}.gif")

    call(("open", "outputs"))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--model", default="THUDM/CogVideoX-5b", required=False)
    parser.add_argument("--prompt", default="sunset in a remote valley in berner oberland", required=False)
    parser.add_argument("--width", default=256, type=int, required=False)
    parser.add_argument("--height", default=256, type=int, required=False)
    parser.add_argument("--inference-steps", default=64, type=int, required=False)
    parser.add_argument("--videos-per-batch", default=1, type=int, required=False)

    arguments = parser.parse_args()
    resolution = arguments.width, arguments.height

    main(arguments.model, arguments.prompt, resolution, arguments.inference_steps, arguments.videos_per_batch)