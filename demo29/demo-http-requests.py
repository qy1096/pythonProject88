'''
## http主要使用部分
1.请求方法:
2.请求地址:
3.请求头：
4.请求体：
5.响应数据：接口基本都是json
'''

# requests库介绍
'''
作用： 提供Http协议的一个第三方库
'''

# 1.请求方法：
# 2.请求地址
# 3.请求头
# 4.请求体
'''
最常见的：
requests.get(url,headers)   get方法没有请求体！！！ body可以传多种数据类型，json只能传json数据类型
requests.post(url,headers,body/json)
requests.put(url,headers)
requests.delete(url,headers)
'''
# 5.响应数据
response = requests.psot("http://www.baidu.com")
'''
查看响应状态码：response.status_code
响应中的编码 ：response.encoding
响应体 ：
     1）文本查看 ：response.text
     2)json查看 ：response.json()
'''





