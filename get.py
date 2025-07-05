from aiohttp import *

async def getzapros(text):
    async with ClientSession() as session:
        async with session.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek/deepseek-r1-distill-llama-70b:free",
                "messages": [
                    {
                        "role": "user",
                        "content": text
                    }
                ],
            },
        ) as response:
            data = await response.json()
            print(data["choices"][0]["message"]["content"])
            return data["choices"][0]["message"]["content"]