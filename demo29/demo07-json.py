'''
案例
1). 访问查询天气信息的接口，并获取JSON响应数据 2). 接口地址：http://www.weather.com.cn/data/
sk/101010100.html
'''
import requests

response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
response.encoding = 'utf-8'

text = response.text
print('查看数据类型：',type(text))
print(text)

''' 这种写法是错误的，因为这个数据类型为字符串，而字符串里没有get调用方法（字典才有）
city1 = text.get('weatherinfo').get('city')
print(city1)
'''

json_data = response.json()
print('查看数据类型：',type(json_data))
print(json_data)
# 下面写法就是正确的，因为字典有get调用方法
city = json_data.get('weatherinfo').get('city')
print(city)