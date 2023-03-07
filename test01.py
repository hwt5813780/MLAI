import requests

 
def main():
  url = 'https://openapi.youdao.com/ocrapi'
  html = requests.get(url).text
  print(html)
 
 
if __name__ == '__main__':
  main()