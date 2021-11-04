# 导包
from conforller import login


# 测试  主要做一个比较的工作：预期结果与实际结果

# assert : 断言  断言不成功会报错，成功不会返回结果

# assert 3 == 4

# case1 : 验证正确的用户名和密码进行登录
assert '登录成功' == login('admin','123456')

# case2 : 验证正确的用户名和密码进行登录
assert '密码不能为空!' == login('admin','')

assert '登录成功' == login('admin','123456')

# 不使用框架测试时一旦遇到错误用例会终止测试，即使后面用例是正确的
