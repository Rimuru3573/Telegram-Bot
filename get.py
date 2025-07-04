from openai import AsyncOpenAI

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
async def getzapros(text):
    completion = await client.chat.completions.create(
    model="deepseek/deepseek-chat:free",
    messages=[
        {
        "role": "user",
        "content": f"{text}"
        }
    ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content