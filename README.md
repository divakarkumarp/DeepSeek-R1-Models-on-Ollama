# DeepSeek-R1-Models-on-Ollama
### Run DeepSeek-R1 🦈 on Your Laptop with Ollama 🦙🦙

This guide will walk you through how to run the latest DeepSeek R1 models locally on your computer using Ollama. DeepSeek R1 is a large language model designed for reasoning and multi-step problem-solving tasks. It leverages Reinforcement Learning (RL) to enhance its logical thinking capabilities.

DeepSeek AI also offers smaller, distilled versions of the model, making it easier to run on personal computers while retaining much of the reasoning power of the larger models.

![Image](https://github.com/user-attachments/assets/3b0d1ca0-d745-47b5-9018-7bf56fad7327)
![Image](https://github.com/user-attachments/assets/c2e90330-2eda-451b-b047-177297b6e031)
![Image](https://github.com/user-attachments/assets/87c02a56-f1a1-4968-88ad-7876ac6761e1)

![Image](https://github.com/user-attachments/assets/58bad876-9853-4bdc-bf54-d43698bc0ae2)
![Image](https://github.com/user-attachments/assets/e221371a-6ed7-4854-a7e0-23b6f0d40462)

## Prerequisites

Before getting started, ensure you have the following set up:

1. **Ollama**: Make sure Ollama is installed and ready to use. You can check the installed version of Ollama by running:
```
ollama -v 
```
## DeepSeek Models on Ollama
DeepSeek models are available on the Ollama library in various sizes and formats. Here's a breakdown:

* **Model Sizes:** 1.5B, 7B, 8B, 14B, 32B, 70B, and 671B parameters.

* **Quantized Versions:** Some models are available in quantized versions (e.g., q4_K_M, q8_0), which use less memory and run faster but may have a slight drop in quality.

* **Distilled Versions:** Smaller models trained to mimic the larger ones, balancing performance and resource usage (e.g., qwen-distill, llama-distill).

* **Tags:** Each model has a latest tag and specific tags indicating size, quantization, and distillation method.

## Pulling a Model
To download a DeepSeek model, use the following commands:

Latest 7B Model:
```
ollama pull deepseek-r1:7b
```

14B Qwen-distilled Model with q4_K_M Quantization:
```
ollama pull deepseek-r1:14b-qwen-distill-q4_K_M
```
70B Llama-distilled Model with fp16 Precision:
```
ollama pull deepseek-r1:70b-llama-distill-fp16
```
## Running a Model
To run a downloaded model, use the following command:

Run the Latest 7B Model:
```
ollama run deepseek-r1:7b
```
## Clone the Repository
```
git clone https://github.com/divakarkumarp/DeepSeek-R1-Models-on-Ollama.git
```
## Setting Up the Environment
Create a Virtual Environment:
```
py -m venv .venv
```
Activate the Virtual Environment:
```
.venv\Scripts\activate
```

Happy coding! 🚀

This `README.md` provides a comprehensive guide for users to set up and run DeepSeek R1 models locally using Ollama. It includes instructions for pulling and running models, setting up the environment, and contributing to the project.
