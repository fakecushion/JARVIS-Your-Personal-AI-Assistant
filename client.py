from openai import OpenAI
import openai

client = OpenAI(
    api_key ="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general task like alexa and google cloud"},
        {
            "role": "user",
            "content": "what is coding"
        }
    ]
)

print(completion.choices[0].message)
