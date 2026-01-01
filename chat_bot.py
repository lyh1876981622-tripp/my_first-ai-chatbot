import gradio as gr
from transformers import pipeline

# 加载模型
generator = pipeline("text-generation", model="Qwen/Qwen1.5-0.5B")

def chat(message, history, temperature, top_p, max_new_tokens):
    # 安全拼接多轮历史（兼容字典格式）
    prompt = ""
    for turn in history:
        if isinstance(turn, dict):
            role = turn.get("role", "")
            content = turn.get("content", "")
            if role == "user":
                prompt += f"用户：{content}\n"
            elif role == "assistant":
                prompt += f"助手：{content}\n"
    prompt += f"用户：{message}\n助手："

    # 生成回应
    result = generator(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        truncation=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    bot_message = result[0]['generated_text'][len(prompt):].strip()

    return bot_message

# 创建界面
demo = gr.ChatInterface(
    fn=chat,
    additional_inputs=[
        gr.Slider(0.1, 1.5, value=0.8, label="温度（创意度）"),
        gr.Slider(0.0, 1.0, value=0.9, label="Top_p（多样性控制）"),
        gr.Slider(50, 300, value=150, step=10, label="最大新生成token数")
    ],
    title="2026最终稳定版AI聊天机器人",
    description="支持多轮上下文记忆与参数调整（兼容最新Gradio）"
)

demo.launch()