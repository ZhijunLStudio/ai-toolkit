import uuid
from pathlib import Path
import torch
from diffusers import FluxPipeline
import datetime
import os

# 指定模型
model_id = "/data/home/lizhijun/llm/flux-hf/models/flux-dev"  # 或者 "black-forest-labs/FLUX.1-dev"

# 加载模型
pipe = FluxPipeline.from_pretrained(model_id, torch_dtype=torch.bfloat16)

# 指定LoRA权重路径
lora_path = "output/my_first_flux_lora_v1/my_first_flux_lora_v1.safetensors"

# 加载LoRA权重
pipe.load_lora_weights(lora_path)

# 启用CPU卸载以节省VRAM
pipe.enable_model_cpu_offload()

# 设置生成参数
prompt = "A photo of circuit diagram."  # 替换为你想要的提示词
seed = 42  # 设置随机种子

# 获取LoRA权重文件名（不包括扩展名）
lora_name = os.path.splitext(os.path.basename(lora_path))[0]

# 创建输出目录
output_dir = "./output_imgs"
Path(output_dir).mkdir(parents=True, exist_ok=True)

# 生成时间戳
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# 生成图像
result = pipe(
    prompt,
    height=1024,
    width=1024,
    guidance_scale=5,
    num_inference_steps=50,
    max_sequence_length=512,
    num_images_per_prompt=5,
    output_type="pil",
    generator=torch.Generator("cpu").manual_seed(seed)
)

# 保存所有生成的图像
for i, image in enumerate(result.images):
    output_file = f"{output_dir}/{lora_name}_{timestamp}_{i+1}.png"
    image.save(output_file)
    print(f"Image {i+1} saved to: {output_file}")

print(f"Total {len(result.images)} images generated and saved.")