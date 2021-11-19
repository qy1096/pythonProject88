
# 完成测试用例的组装和生成测试报告

# 将下载的HTMLTestRunner包放到项目下，然后导入
import unittest
from HTMLTestRunner import HTMLTestRunner
from setting import File_name, LOGIN_INFO
from apis.base import Base

if __name__ == '__main__':

    Base().login(LOGIN_INFO.get('username'), LOGIN_INFO.get('password'))

    suite = unittest.TestLoader().discover('./casess','test*.py')

    with open(File_name,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)





