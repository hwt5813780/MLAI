import openai
import requests
import json

openai.api_key = "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" # 将 YOUR_API_KEY 替换为您的实际 API 密钥

# 设置API请求的URL和参数
url = "https://api.openai.com/v1/chat/completions"

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "你是一个合同信息提取机器人，接下来我会用：“A：合同内容//B：合同信息提示”给你多个prompt，你需要返回给我一个数组，数组的格式为：[{\"prompt\":\"prompt的内容\",\"value\":\"提取的内容\"}]"},
        {"role": "user", "content": "A：甲方购房总价款是12000元，税费为3%//B：甲方购房总价款，甲方购房税费"},
        {"role": "assistant", "content": "[{\"prompt\":\"甲方购房总价款\",\"value\":\"12000元\"},{\"prompt\":\"甲方购房税费\",\"value\":\"360元\"}]"},
        {"role": "user", "content": "A：今天是暴风雪转多云转阴天气，小李的工资为10000元，社保为工资的3%//B：小李的工资金额，小李的社保金额，社保的比例，现在是否下雪"}
    ]
}

headers={"authority": "api.openai.com",
         "Content-Type": "application/json",
         "Authorization": f"Bearer {openai.api_key}"
}

proxies={'http': 'socks5://127.0.0.1:10808',
         'https': 'socks5://127.0.0.1:10808'
}

# 发送HTTP请求
response = requests.post(url, headers=headers,json=data,proxies=proxies)

# 解析响应并输出结果
if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"].strip())
else:
    raise Exception(f"Request failed with status code {response.status_code}")