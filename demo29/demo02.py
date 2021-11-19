# 请求百度
# 1.导包
import requests

reponse = requests.get("http://www.baidu.com")
print(reponse.text)