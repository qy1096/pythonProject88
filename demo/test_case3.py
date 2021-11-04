import unittest
from conforller import login
from parameterized import parameterized


class testlogin(unittest.TestCase):
    #  使用参数化一次实现3条测试用例：

    @parameterized.expand([('登录成功', 'admin', '123456'), ('用户名不能为空', '', '123456'), ('密码不能为空', 'admin', '')])
    def test_login(self, expect, username, password):
        self.assertEqual(expect, login(username, password))

    # # case1 : 验证正确的用户名和密码进行登录
    # def test_login1(self):
    #     print('执行测试用例1')
    #     self.assertEqual('登录成功',login('admin','123456'))
    #
    #
    # # case2 : 验证正确的用户名和空的密码进行登录
    # 跳过执行:
    #@unittest.skip('此测试用例正在开发，暂不执行')
    # def test_login2(self):
    #     print('执行测试用例2')
    #     self.assertEqual('用户名不能为空', login('','123456'))
    #
    # # case3 : 验证密码不为空
    # def test_login3(self):
    #     print('执行测试用例3')
    #     self.assertEqual('密码为空',login('admin',''))
