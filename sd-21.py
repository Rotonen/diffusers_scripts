#!/usr/bin/env python3
from argparse import ArgumentParser
from subprocess import call
from time import time

from diffusers import StableDiffusionPipeline
from slugify import slugify
from torch import bfloat16


def main(model, prompt, resolution, inference_steps, images_per_batch):
    width, height = resolution

    prompt = [prompt] * images_per_batch

    negative_attributes = (
        "low quality",
        "bad quality",
        "ugly",
        "deformed",
        "disfigured",
        "poor details",
        "bad anatomy",
        "unaesthetic",
    )
    negative_prompt = [", ".join(negative_attributes)] * images_per_batch

    datatype = bfloat16

    pipeline = StableDiffusionPipeline.from_pretrained(model, torch_dtype=datatype)
    pipeline.enable_sequential_cpu_offload()
    pipeline.vae.enable_slicing()
    pipeline.vae.enable_tiling()
    pipeline.to(datatype)

    images = pipeline(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=inference_steps,
        width=width,
        height=height,
    ).images

    slugified_prompt = slugify(prompt[0])
    slugified_model_name = slugify(model)
    for image in images:
        try:
            image.save(f"outputs/{time()}-{slugified_model_name}-{width}-{height}-{slugified_prompt}.png")
        except OSError:
            image.save(f"outputs/{time()}-{slugified_model_name}-{width}-{height}.png")

    call(("open", "outputs"))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--model", default="stabilityai/stable-diffusion-2-1", required=False)
    parser.add_argument("--prompt", default="sunset in a remote valley in berner oberland", required=False)
    parser.add_argument("--width", default=1024, type=int, required=False)
    parser.add_argument("--height", default=1024, type=int, required=False)
    parser.add_argument("--inference-steps", default=64, type=int, required=False)
    parser.add_argument("--images-per-batch", default=1, type=int, required=False)

    arguments = parser.parse_args()
    resolution = arguments.width, arguments.height

    main(arguments.model, arguments.prompt, resolution, arguments.inference_steps, arguments.images_per_batch)
