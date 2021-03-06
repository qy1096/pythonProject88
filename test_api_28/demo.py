# 自动化框架 会使用到的知识点

# 1.日志 ：loguru
from loguru import logger
logger.info('这是一条日志')

# 2.测试框架 ：unittest
'''
测试用例 ：Testcase
测试套件 ：TestSuite
测试搜索 ：TestLogder.discover()
'''

# 3.HtmlTestRunner:
'''
类：HtmlTestRunner(),可以生成测试报告
'''

# 4.requests
'''
请求方法
'''

# 5.cache
'''
作用：可以将数据直接保存到缓存中（快速存取数据）
存：cache.set(key,value)
取：cache.get(key)
'''