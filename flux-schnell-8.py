#!/usr/bin/env python3
from argparse import ArgumentParser
from subprocess import call
from time import time

from diffusers import FluxPipeline, FluxTransformer2DModel
from optimum.quanto import freeze, qfloat8, quantize
from slugify import slugify
from torch import bfloat16
from transformers import T5EncoderModel


def main(model, prompt, resolution, inference_steps, images_per_batch):
    width, height = resolution

    prompt = [prompt] * images_per_batch

    datatype = bfloat16
    weights = qfloat8

    transformer = FluxTransformer2DModel.from_single_file(
        "https://huggingface.co/Kijai/flux-fp8/blob/main/flux1-schnell-fp8-e4m3fn.safetensors", torch_dtype=datatype
    )
    quantize(transformer, weights=weights)
    freeze(transformer)

    text_encoder_2 = T5EncoderModel.from_pretrained(model, subfolder="text_encoder_2", torch_dtype=datatype)
    quantize(text_encoder_2, weights=weights)
    freeze(text_encoder_2)

    pipeline = FluxPipeline.from_pretrained(model, transformer=None, text_encoder_2=None, torch_dtype=datatype)
    pipeline.transformer = transformer
    pipeline.text_encoder_2 = text_encoder_2
    pipeline.enable_model_cpu_offload()

    images = pipeline(
        prompt=prompt,
        guidance_scale=0.0,
        num_inference_steps=inference_steps,
        max_sequence_length=256,
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

    parser.add_argument("--model", default="black-forest-labs/FLUX.1-schnell", required=False)
    parser.add_argument("--prompt", default="sunset in a remote valley in berner oberland", required=False)
    parser.add_argument("--width", default=1024, type=int, required=False)
    parser.add_argument("--height", default=1024, type=int, required=False)
    parser.add_argument("--inference-steps", default=4, type=int, required=False)
    parser.add_argument("--images-per-batch", default=1, type=int, required=False)

    arguments = parser.parse_args()
    resolution = arguments.width, arguments.height

    main(arguments.model, arguments.prompt, resolution, arguments.inference_steps, arguments.images_per_batch)
