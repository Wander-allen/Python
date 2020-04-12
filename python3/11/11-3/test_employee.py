import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """一个统计员工信息的方法"""
    def setUp(self):
        self.employee1 = Employee('zhao','qian',20000)
        self.result1 = 20000
        self.employee2 = Employee('zhao','qian')
        self.result2 = 5000


    def test_give_default_raise(self):
        """测试默认薪水的方法"""
        self.assertEqual(self.result1,self.employee1.give_raise())

    def test_give_custom_raise(self):
        """测试非默认薪水的方法"""
        self.assertEqual(self.result2,self.employee2.give_raise())
        
unittest.main()
