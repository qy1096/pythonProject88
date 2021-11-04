import unittest


# 所有的测试用例都从该入口去运行，从这个里面去组装套件，然后运行套件

# 1：创建套件
suite = unittest.TestLoader().discover('.',pattern='test*.py')

# 2：创建运行器：
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)


