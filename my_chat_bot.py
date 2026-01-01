import gradio as gr
from transformers import pipeline


generator = pipeline("text-generation", model="Qwen/Qwen1.5-0.5B")

def chat(message, history):
    # 把历史对话 + 新消息拼接成输入
    input_text = message
    result = generator(input_text, max_length=200, do_sample=True, temperature=0.8, top_p=0.9)
    return result[0]['generated_text']

# 创建网页界面
demo = gr.ChatInterface(
    fn=chat,
    title="我的2026 AI聊天机器人（by 我自己）",
    description="输入任何话，让AI陪你聊天、帮你出主意、写攻略～"
)

demo.launch(share=False)  # 本地运行，浏览器会自动打开