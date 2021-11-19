
# 主要实现的是用户管理的测试用例
from apis.user_manager_api import UserManageApi
import unittest

class TestUserManagerCase(unittest.TestCase):

    user_id = 86

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManageApi()


    # 实现添加测试用例：
# 测试用例一定要写编号确定运行顺序
    def test01_add_user(self):
        #1.定义数据
        username = 'qqqc16'
        password = 'qqqc16'
        #2.调用添加管理员接口
        result = self.user.add_user(username,password)
        # 获取id值
        if result.get('data').get('id'):
            TestUserManagerCase.user_id = result.get('data').get('id')
        #3.进行断言
        self.assertEqual(0,result.get('errno'))

    # 实现编辑测试用例：
    def test02_edit_user(self):
        # 1.定义数据
        new_user = 'qqqc15'
        password = 'qqqc15'
        # 2.调用编辑接口
        result = self.user.edif_user(TestUserManagerCase.user_id,new_user,password)
        # 3.进行断言
        self.assertEqual(0,result.get('errno'))

    # 实现删除测试用例：
    def test03_delete_user(self):
        new_user = 'qqqc15'
        password = 'qqqc15'
        result = self.user.delete_user(TestUserManagerCase.user_id,new_user,password)
        self.assertEqual(0, result.get('errno'))
    # 实现查询测试用例：
    def test04_get_user(self):
        result = self.user.get_user()
        self.assertEqual(0, result.get('errno'))






