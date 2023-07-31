import torch
import imageio
from direct2v_zeroshot import DirecT2VPipeline
from diffusers import TextToVideoZeroPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipe_ours = DirecT2VPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
pipe_t2vz = TextToVideoZeroPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

# Fixed prompt (Text2Video-Zero)
prompt = "A corgi is running and another corgi joins."

# Frame-level prompt by GPT-4 (Ours)
prompts = [
    "A corgi is running on a grassy field, its ears flopping as it moves.",
    "The corgi continues running, a second corgi starts to appear in the background.",
    "The second corgi starts to run, playfully chasing the first corgi.",
    "The first corgi maintains its pace, the second corgi getting closer.",
    "Both corgis are running side by side, their short legs moving quickly.",
    "The second corgi starts to take the lead, the first corgi following closely.",
    "Both corgis continue running, their tails wagging happily as they race.",
    "The first corgi begins to catch up, the two corgis running neck and neck.",
]

# Text2Video-Zero sample
result = pipe_t2vz(prompt=prompt, generator=torch.Generator('cuda').manual_seed(10)).images
result = [(r * 255).astype("uint8") for r in result]
imageio.mimsave("video_t2vz.mp4", result, fps=6)

# DirecT2V sample
result = pipe_ours(prompt=prompts, generator=torch.Generator('cuda').manual_seed(10)).images
result = [(r * 255).astype("uint8") for r in result]
imageio.mimsave("video_ours.mp4", result, fps=6)
