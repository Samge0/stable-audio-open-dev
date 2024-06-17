#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-06-12 16:18
# describe：

import os
import time
import torch
import torchaudio
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond
from huggingface_hub import login


"""
generation takes about 100 seconds
"""

stat_time = time.time()

# Login to Hugging Face，Get The Token Here：https://huggingface.co/settings/tokens
HUGGINGFACE_TOKEN = os.environ["HUGGINGFACE_TOKEN"]
if not HUGGINGFACE_TOKEN:
    raise ValueError("HUGGINGFACE_TOKEN environment variable not configured")
login(HUGGINGFACE_TOKEN)


device = "cuda" if torch.cuda.is_available() else "cpu"

# Download model
model, model_config = get_pretrained_model("stabilityai/stable-audio-open-1.0")
sample_rate = model_config["sample_rate"]
sample_size = model_config["sample_size"]

model = model.to(device)

# prompt = "soft and melancholic piano music with a gentle, sorrowful melody"
# prompt = "Rock beat played in a treated studio, session drumming on an acoustic kit"
prompt = "upbeat and rhythmic electronic dance music with a catchy melody and strong bassline"

# Set up text and timing conditioning
conditioning = [{
    "prompt": prompt,
    "seconds_start": 0, 
    "seconds_total": 30
}]

# Generate stereo audio，the first run will automatically download the model from the huggingface
output = generate_diffusion_cond(
    model,
    steps=100,
    cfg_scale=7,
    conditioning=conditioning,
    sample_size=sample_size,
    sigma_min=0.3,
    sigma_max=500,
    sampler_type="dpmpp-3m-sde",
    device=device
)

# Rearrange audio batch to a single sequence
output = rearrange(output, "b d n -> d (b n)")

# makedirs
output_path = f".cache/output{int(time.time())}.wav"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Peak normalize, clip, convert to int16, and save to file
output = output.to(torch.float32).div(torch.max(torch.abs(output))).clamp(-1, 1).mul(32767).to(torch.int16).cpu()
torchaudio.save(output_path, output, sample_rate)

print(f'save in:"{output_path}:{output_path}"')
print(f"all down，{time.time() - stat_time}s")