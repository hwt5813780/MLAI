import requests
import openai
openai.api_key = "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"
proxies= {
    "http":"http://127.0.0.1:7890",
    "https":"http://127.0.0.1:7890",
}

headers = {"authority": "api.openai.com",
           "Content-Type": "application/json",
           "Authorization": f"Bearer {openai.api_key}"
           }

def main():
  url = 'https://api.openai.com/v1/images/generations'
  data = {
          "prompt": "A cute baby sea otter",
          "n": 1,
          "size": "1024x1024"
        }

  response = requests.post(url,headers=headers,json=data, proxies=proxies)
  print(response.text)
 
 
if __name__ == '__main__':
  main()