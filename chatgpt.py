import os
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
print(completion.choices[0].message)