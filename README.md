# Large Language Models are Frame-level Directors for Zero-shot Text-to-Video Generation
<a href="https://arxiv.org/abs/2305.14330"><img src="https://img.shields.io/badge/arXiv-2305.14330-B31B1B"></a>

## 🎥 Zero-shot Video Demo## 📰 Abstract



https://github.com/KU-CVLAB/DirecT2V/assets/5498512/b721aa65-8156-4fdc-a371-db6eda6b6f55


>In the paradigm of AI-generated content (AIGC), there has been increasing attention in extending pre-trained text-to-image (T2I) models to text-to-video (T2V) generation. Despite their effectiveness, these frameworks face challenges in maintaining consistent narratives and handling rapid shifts in scene composition or object placement from a single user prompt. This paper introduces a new framework, dubbed DirecT2V, which leverages instruction-tuned large language models (LLMs) to generate frame-by-frame descriptions from a single abstract user prompt. DirecT2V utilizes LLM directors to divide user inputs into separate prompts for each frame, enabling the inclusion of time-varying content and facilitating consistent video generation. To maintain temporal consistency and prevent object collapse, we propose a novel value mapping method and dual-softmax filtering. Extensive experimental results validate the effectiveness of the DirecT2V framework in producing visually coherent and consistent videos from abstract user prompts, addressing the challenges of zero-shot video generation. The code and demo will be publicly availble.

![image](https://github.com/KU-CVLAB/DirecT2V/assets/5498512/3176b105-a0f0-4363-9189-f54f0569908e)

**Overall pipeline of DirecT2V.** Our framework consists of two parts: directing an abstract user prompt with an LLM director (GPT-4) and video generation with a modified T2I diffusion (Stable Diffusion).

## 🔥 We are working on the code and an interactive demo. Stay in touch!
