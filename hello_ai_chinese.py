from transformers import pipeline

# 用一个支持中文的小模型：Qwen1.5-0.5B（只有几百MB，CPU跑得快）
generator = pipeline("text-generation", model="Qwen/Qwen1.5-0.5B")

# 输入你的励志句，让它接下去
result = generator(
    "2026年，我要成为一个超强的AI工程师，因为",
    max_length=100,  # 生成更长一点
    num_return_sequences=1,
    temperature=0.8,  # 让输出更有创意
    do_sample=True
)
print(result[0]['generated_text'])