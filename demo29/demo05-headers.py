import requests
url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username":"admin123","password":"admin123"}
headers = {'ContentType':'application/json'}
response1 = requests.post(url,json=login_data,headers=headers)
print(response1.text)

# 当数据类型为json时headers默认为application/json，数据类型为data是headers默认为表单

url = "http://121.196.13.152:8080/admin/auth/login"
login_data = '{"username":"admin123","password":"admin123"}'
headers = {'ContentType':'application/json'}
response1 = requests.post(url,data=login_data,headers=headers)
print(response1.text)