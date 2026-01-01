# 我的第一个AI聊天机器人（2026开局项目）

## 项目描述
使用Hugging Face Transformers和Gradio，搭建了一个基于Qwen1.5-0.5B模型的本地聊天机器人。支持实时中文对话、续写文本。

## 运行步骤
1. conda create -n ai_start python=3.10
2. conda activate ai_start
3. pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
4. pip install transformers gradio
5. python my_chat_bot.py

## 技术栈
- Python
- Transformers (Qwen1.5-0.5B)
- Gradio网页界面
