import os
import openai
 
openai.api_key = "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"


def chat(prompt):  #定义一个函数

    try:
        response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "user", "content": prompt}]
                )

        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as exc:
        #print(exc)  #需要打印出故障
        return "broken"



result = chat("一句话描述一下今天的天气")
print('ChatGPT：'+result)