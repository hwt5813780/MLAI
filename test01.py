import requests

 
def main():
  url = 'https://api.openai.com/v1/chat/completions'
  html = requests.get(url).text
  print(html)
 
 
if __name__ == '__main__':
  main()