import unittest
from conforller import login


class testlogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print('开始测试')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('结束测试')
    #
    # # 初始化方法
    # def setUp(self) -> None:
    #     print('执行初始化工作')
    #
    # # 清空方法
    # def tearDown(self) -> None:
    #     print('执行清空工作')


    # case1 : 验证正确的用户名和密码进行登录
    def test_login1(self):
        print('执行测试用例1')
        self.assertEqual('登录成功',login('admin','123456'))


    # case2 : 验证正确的用户名和空的密码进行登录
    def test_login2(self):
        print('执行测试用例2')
        self.assertEqual('用户名不能为空', login('','123456'))

    # case3 : 验证密码不为空
    def test_login3(self):
        print('执行测试用例3')
        self.assertEqual('密码为空',login('admin',''))

# 创建套件
# 第一种 一个一个传用例
# suite = unittest.TestSuite()
# suite.addTest(testlogin('test_login2'))
# suite.addTest(testlogin('test_login3'))

# 第二种 先创建列表，批量传用例  注意：使用的是 addTests
# case_list = [testlogin('test_login2'),testlogin('test_login3')]
# suite.addTests(case_list)
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

# suite_smoke = unittest.TestSuite()
# suite_smoke.addTest(testlogin('test_login1'))

