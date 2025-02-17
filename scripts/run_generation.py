import comfyui
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")
prompt = "A futuristic cityscape with neon lights"
image = pipe(prompt).images[0]

output_path = "outputs/generated_image.png"
image.save(output_path)
print(f"Image saved at {output_path}")
