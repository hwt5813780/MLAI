import os
import openai

openai.api_key = "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"
print("if you want to stop the conversation, please input 'quit'") #提示想终止聊天时输入"quit"


def chat(prompt):  #定义一个函数

    try:
        response = openai.ChatCompletion.create(
                  model="gpt-3.5-turbo",
                  messages=[{"role": "user", "content": prompt} ]
                )

        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as exc:
        #print(exc)  #需要打印出故障
        return "broken"


while True: #能够连续提问
    question = input()
    if len(question.strip()) == 0: #如果输入为空，提醒输入问题
        print("please input your question")
    elif question == "quit":  #如果输入为"quit"，程序终止
        print("\nAI: See You Next Time!")
        break
    else:
        prompt = question
        result = chat(prompt)
        print('ChatGPT：'+result)