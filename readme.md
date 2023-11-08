# AI 开发快速入门
前置说明:  
1. 本课程主要服务于已经有编程基础，且想接触ai开发的开发人员  
1. 本课程的目标是在课程结束后，开发人员可以灵活运用习得的知识将开源的AI项目做一定程度的适配改动并应用在自己的业务中  
1. 本课程主要基于 nvidia 生态，但学习阶段对电脑的配置要求不高，2G 的显存即可支持本课程中的练习  

## 课程大纲
c1-environment - ai 开发环境准备，包含 nvidia驱动/cuda/cudnn/python/pytorch 的环境准备工作  
c2-autograde_and_baseex - ai 训练的简单理论基础演示与一个小型的实战项目  
c3-hugging_face_base - hugging face 平台的介绍与基础使用，并包含一个 gpt2 项目基础运行展示  
c4-hugging_face_lora - 以 gpt2 为案例的 lora 训练  
c5-gradio - 简单介绍和展示 gradio 的相关功能，以及其在业务工程开发中的定位  

## 课程详细内容导航
### c1-environment
1. 基础环境配置 - [c1-environment/c1-base.md](/c1-environment/c1-base.md)  
1. python环境配置 - [c1-environment/c1-base.md](/c1-environment/c1-base.md)  

### c2-autograde_and_baseex
1. 自动求导与ai训练中的关系 - [c2-autograd_and_baseex/c2-main.md](/c2-autograd_and_baseex/c2-main.md)  
1. ai训练处理波士顿房价预测（实战） - [c2-autograd_and_baseex/c2-bostan.md](/c2-autograd_and_baseex/c2-bostan.md)  
1. 链式法则简要说明 - [c2-autograd_and_baseex/c2-grad-chain.md](/c2-autograd_and_baseex/c2-grad-chain.md)  

代码相关:  
1. pytorch 自动求导展示 - [c2-autograd_and_baseex/autograd.py](/c2-autograd_and_baseex/autograd.py)  
1. 波士顿房价预测模型训练 - [c2-autograd_and_baseex/bostan_train.py](/c2-autograd_and_baseex/bostan_train.py)  
1. 波士顿房价预测模型使用 - [c2-autograd_and_baseex/bostan_infer.py](/c2-autograd_and_baseex/bostan_infer.py)  

### c3-hugging_face_base
1. huggingface基础与简单使用案例解析 - [c3-hugging_face_base/c3.md](/c3-hugging_face_base/c3.md)  
1. gpt2 推理代码案例 - [c3-hugging_face_base/gpt2-infer.ipynb](/c3-hugging_face_base/gpt2-infer.ipynb)  

### c4-hugging_face_lora
1. lora 原理机制说明 - [c4-hugging_face_lora/lora.md](/c4-hugging_face_lora/lora.md)  
1. 模型训练相关解析 - [c4-hugging_face_lora/c4.md](/c4-hugging_face_lora/c4.md)  

代码相关:  
1. 模型训练代码案例 - [c4-hugging_face_lora/gpt2-trainer.ipynb](/c4-hugging_face_lora/gpt2-trainer.ipynb)  
1. 使用训练后端的 lora 运行模型案例 - [c4-hugging_face_lora/gpt2-run.ipynb](/c4-hugging_face_lora/gpt2-run.ipynb)  

### c5-gradio
1. gradio 的介绍与使用 - [c5-gradio/c5.md](/c5-gradio/c5.md)  

## 后续计划
ai 绘画，语音合成，歌曲合成，lipsync 等常见场景的扩展课程  
