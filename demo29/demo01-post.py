# 请求tpshop的登录接口

# 1.导包
import requests

# 2.请求psot方法，传递表单类型
url =  "http://localhost/index.php?m=Hmoe&c=User&a=do_login"
login_data = {"username":"13088888888","password":"123456","verify_code":"1234"}
response = requests.post(url,data=login_data)
print(response.text)