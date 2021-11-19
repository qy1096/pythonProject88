import requests
url = "http://121.196.13.152:8080/admin/auth/login"
login_data = {"username":"admin123","password":"admin123"}
response1 = requests.post(url,json=login_data)
print(response1.text)