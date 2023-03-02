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

text = "" #设置一个字符串变量
turns = [] #设置一个列表变量，turn指对话时的话轮
while True: #能够连续提问
    question = input()
    if len(question.strip()) == 0: #如果输入为空，提醒输入问题
        print("please input your question")
    elif question == "quit":  #如果输入为"quit"，程序终止
        print("\nAI: See You Next Time!")
        break
    else:
        prompt = text + "\nuser: " + question
        result = chat(prompt)
        while result == "broken": #问不出结果会自动反复提交上一个问题，直到有结果为止。
            print("please wait...")
            result = chat(prompt) #重复提交问题
        else:
            turns += [question] + [result]#只有这样迭代才能连续提问理解上下文
            print(result)
        if len(turns)<=10:   #为了防止超过字数限制程序会爆掉，所以提交的话轮语境为10次。
            text = " ".join(turns)
        else:
            text = " ".join(turns[-10:]) 