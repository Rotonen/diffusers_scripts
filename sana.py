#!/usr/bin/env python3
from argparse import ArgumentParser, BooleanOptionalAction
from subprocess import call
from time import time

from diffusers import SanaPipeline
from slugify import slugify
from torch import bfloat16, float32


def main(arguments):
    model = arguments.model
    prompt = arguments.prompt
    width = arguments.width
    height = arguments.height
    inference_steps = arguments.inference_steps
    images_per_batch = arguments.images_per_batch
    open_outputs = arguments.open_outputs

    prompt = [prompt] * images_per_batch

    pipeline = SanaPipeline.from_pretrained(model, torch_dtype=float32)

    pipeline.to("cuda")
    pipeline.text_encoder.to(bfloat16)
    pipeline.transformer = pipeline.transformer.to(bfloat16)

    images = pipeline(
        prompt=prompt,
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

    if open_outputs:
        call(("open", "outputs"))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--model", default="Efficient-Large-Model/Sana_1600M_1024px_BF16_diffusers", required=False)
    parser.add_argument("--prompt", default="sunset in a remote valley in berner oberland", required=False)
    parser.add_argument("--width", default=1024, type=int, required=False)
    parser.add_argument("--height", default=1024, type=int, required=False)
    parser.add_argument("--inference-steps", default=32, type=int, required=False)
    parser.add_argument("--images-per-batch", default=1, type=int, required=False)
    parser.add_argument("--open-outputs", default=True, action=BooleanOptionalAction, required=False)

    arguments = parser.parse_args()

    main(arguments)
