# 🤖 🌄 comfyui-docker

## 🚀 Dockerized AI Environment with NVIDIA CUDA for ComfyUI

Docker setup for a powerful and modular diffusion model GUI and backend. 

This project sets up a complete AI development environment with NVIDIA CUDA, cuDNN, and various essential AI/ML libraries using Docker. It includes Stable Diffusion models and ControlNet for text-to-image generation and various deep learning models.

## 🛠️ Project Overview

This Docker image is based on **`nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04`**, ensuring GPU acceleration for deep learning workloads. It is configured for ease of use with `Pyenv`, custom Python versions, and GPU-specific libraries.

### Key Features:

- **NVIDIA CUDA & cuDNN** support for GPU-accelerated AI tasks.
- **Pyenv** for managing Python versions.
- Integration with **ComfyUI**, **Stable Diffusion**, and **ControlNet** models.
- **Custom node installation** for advanced workflows and extensions.
- Ready-to-use **AI/ML models** from Hugging Face, including various **checkpoints** for text-to-image generation.

## 🛠️ Setup

### Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- NVIDIA GPU with proper drivers.
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) (for GPU acceleration).

### Steps to Build and Run

1. **Clone the repository** and navigate to the project root:

   ```bash
   git clone https://github.com/krasamo/comfyui-docker.git
   cd https://github.com/krasamo/comfyui-docker.git
   ```

2. **Build the Docker image**:

   ```bash
   docker-compose build
   ```

3. **Run the Docker container**:

   ```bash
   docker-compose up
   ```

   The service will run on port `7860`, accessible via `http://localhost:7860`.

## 🔧 Customization

You can modify the Docker build to suit your needs by adding models or adjusting the configuration.

### Example: Persistent Data

To enable persistent data storage, pass the `USE_PERSISTENT_DATA` argument:

```bash
docker-compose up -d
```

This will store outputs and models in `/data` on the host machine, ensuring that checkpoints and configurations are preserved.

## 🧠 Included AI Models

This Docker setup automatically downloads several pre-trained models from Hugging Face, including:

- **Stable Diffusion XL**: High-quality text-to-image models.
- **ControlNet**: Pretrained models for image control.
- **ESRGAN**: For super-resolution upscaling.

Refer to the Dockerfile for the exact models included and their paths.

## 📂 Directory Structure
The configuration which is quite complex with the addition of scripting knowledge for the AI-powered image generation  makes the non professional folks a bit uncomfortable with the process.

The technical barrier which is prominent among users, could be addressed by the pipeline of image production, which is efficient, creative and customized. The previous models of text to image generation are not adaptable across the industrial methods. Hence, these are not user-friendly.

ComfyUI has the feature of optimized GPU usage with batch processing to generate images faster. The creator could generate their creativity into efficient piece of work.
ComfyUI helps user to explore more possibilities with advanced models like Stable Diffusion.
The applications includes the content creation, gaming, digital art and advertising. With the simplification of workflows, more users could utilize the AI generated images for commercial objectives.
Stable Diffusion utilizes the  Variational Auto Encoder(VAE) encodes images from the latent space. The latent space contains lower resolution and higher representation of any source image.

VAE learns by itself during the training phase, which leads to different versions of model, as it gets trained frequently. 
VAE encodes higher resolution features.
Latent representation is utilized by the algorithm of Stable Diffusion, while generating the images from text related prompts. 
The process starts with the iteration of noises produced inside the latent representation of the models, training of U-Net is done by telling it information about the noise.
VAE-based are efficient in encoding and decoding images from latent spaces, and for the training of diffusion models inside a low-dimensional latent space, VQ-GAN model works as an autoencoder.
DALL-E 2 is also known as unclip uses diffusion model inside, which operates on latent code. The diffusion prior, converts the text embedding into image embedding


- `/models`: Contains all downloaded models (checkpoints, VAE, Loras, etc.).
- `/code`: Working directory for the main codebase.
- `/data`: Optional directory for persistent data, checkpoints, and output.

## 🛠️ How to Add Custom Models

You can add custom models by modifying the `Dockerfile` and adding additional `wget` commands to download models or use external repositories.

For example, add the following to download a custom checkpoint:

```bash
RUN wget -c <model-url> -P ./models/checkpoints/
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙌 Acknowledgments

- NVIDIA for CUDA and GPU acceleration.
- Hugging Face for pre-trained AI models.
- Stability AI for Stable Diffusion.

- Python 3.11 as programming language, and frameworks like PyTorch, Hugging Face Diffusers and ComfyUI.
GPU required are: cuDNN, NVIDIA Toolkit, and CUDA.
Operating System such as Linux(Ubuntu),Windows, and macOS are effiecient.
Virtual environment can be utilized such as conda or venv for the management of dependencies.
AWS, GCP and Azure could be utilized for deployment.

Image generated through prompt:

![image](https://github.com/user-attachments/assets/be6008a1-e59f-45e2-b96c-edf3f7b8cbf5)


---

Feel free to modify or expand upon this depending on your specific project needs!
