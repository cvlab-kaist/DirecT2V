# Large Language Models are Frame-level Directors for Zero-shot Text-to-Video Generation
**Susung Hong\quad Junyoung Seo\quad Sunghwan Hong\quad Heeseong Shin\quad Seungryong Kim**

## Zero-shot Video Demo

https://github.com/KU-CVLAB/DirecT2V/assets/5498512/28b48f0b-a2bc-47ed-ac7b-b46f25c0b37c

## Abstract
>In the paradigm of AI-generated content (AIGC), there has been increasing attention in extending pre-trained text-to-image (T2I) models to text-to-video (T2V) generation. Despite their effectiveness, these frameworks face challenges in maintaining consistent narratives and handling rapid shifts in scene composition or object placement from a single user prompt. This paper introduces a new framework, dubbed DirecT2V, which leverages instruction-tuned large language models (LLMs) to generate frame-by-frame descriptions from a single abstract user prompt. DirecT2V utilizes LLM directors to divide user inputs into separate prompts for each frame, enabling the inclusion of time-varying content and facilitating consistent video generation. To maintain temporal consistency and prevent object collapse, we propose a novel value mapping method and dual-softmax filtering. Extensive experimental results validate the effectiveness of the DirecT2V framework in producing visually coherent and consistent videos from abstract user prompts, addressing the challenges of zero-shot video generation. The code and demo will be publicly availble.

![image](https://github.com/KU-CVLAB/DirecT2V/assets/5498512/3176b105-a0f0-4363-9189-f54f0569908e)

**Overall pipeline of DirecT2V.** Our framework consists of two parts: directing an abstract user prompt with an LLM director (GPT-4) and video generation with a modified T2I diffusion (Stable Diffusion).

## 🔥We are working on the code and an interactive demo. Stay in touch!
