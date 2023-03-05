import requests
 
import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10808)
socket.socket = socks.socksocket
 
def main():
  url = 'https://www.google.com'
  html = requests.get(url).text
  print(html)
 
 
if __name__ == '__main__':
  main()