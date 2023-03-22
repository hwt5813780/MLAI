import os
import openai
openai.api_key = "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"
response = openai.Image.create(
    prompt="A cute baby sea otter",
    n=2,
    size="512x512"
)

image_url = response['data'][0]['url']
