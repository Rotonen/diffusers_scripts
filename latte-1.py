#!/usr/bin/env python3
from argparse import ArgumentParser, BooleanOptionalAction
from subprocess import call
from time import time

from diffusers import LattePipeline
from diffusers.utils import export_to_gif
from slugify import slugify
from torch import bfloat16


def main(arguments):
    model = arguments.model
    prompt = arguments.prompt
    width = arguments.width
    height = arguments.height
    inference_steps = arguments.inference_steps
    videos_per_batch = arguments.videos_per_batch
    open_outputs = arguments.open_outputs

    prompt = [prompt] * videos_per_batch

    datatype = bfloat16

    pipeline = LattePipeline.from_pretrained(model, torch_dtype=datatype)
    pipeline.enable_model_cpu_offload()
    pipeline.to(datatype)

    videos = pipeline(
        prompt=prompt,
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

    if open_outputs:
        call(("open", "outputs"))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--model", default="maxin-cn/Latte-1", required=False)
    parser.add_argument("--prompt", default="sunset in a remote valley in berner oberland", required=False)
    parser.add_argument("--width", default=256, type=int, required=False)
    parser.add_argument("--height", default=256, type=int, required=False)
    parser.add_argument("--inference-steps", default=64, type=int, required=False)
    parser.add_argument("--videos-per-batch", default=1, type=int, required=False)
    parser.add_argument("--open-outputs", default=True, action=BooleanOptionalAction, required=False)

    arguments = parser.parse_args()

    main(arguments)
