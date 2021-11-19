'''
案例
1. 访问百度首页的接口 http://www.baidu.com ，获取以下响应数据
2. 获取响应状态码
3. 获取请求URL
4. 获取响应字符编码
5. 获取响应头数据
6. 获取文本形式的响应内容
'''

import requests
response = requests.get("http://www.baidu.com")

print('查看响应状态码：',response.status_code)
print('查看请求的url地址：',response.url)
print('查看编码：',response.encoding)
print('查看响应数据：',response.text)

# 设置编码
response.encoding = 'utf-8'  # 转化为中文
print('查看编码后的数据：',response.text)