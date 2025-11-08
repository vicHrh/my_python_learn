"""
第一阶段练习：基础语法 - 计算器程序
目标：熟悉Python基本语法、数据类型和控制结构
"""


# 练习1：基础运算函数
def add(a, b):
    """实现加法运算"""
    # TODO: 实现加法逻辑
    a + b
    pass


def subtract(a, b):
    """实现减法运算"""
    # TODO: 实现减法逻辑
    a - b
    pass


def multiply(a, b):
    """实现乘法运算"""
    # TODO: 实现乘法逻辑
    a * b
    pass


def divide(a, b):
    """实现除法运算，注意处理除零错误"""
    # TODO: 实现除法逻辑，添加异常处理
    pass


# 练习2：数字分类函数
def number_category(num):
    """
    根据数字的特性返回其分类
    - 如果是负数，返回 "negative"
    - 如果是正数，返回 "positive"
    - 如果是零，返回 "zero"
    - 如果是偶数，额外添加 "even" 特性
    - 如果是奇数，额外添加 "odd" 特性
    
    返回格式示例："positive even" 或 "negative odd"
    """
    # TODO: 实现数字分类逻辑
    pass


# 练习3：列表操作函数
def list_operations():
    """
    创建一个函数演示Python列表的基本操作：
    - 创建一个空列表
    - 添加元素
    - 插入元素
    - 删除元素
    - 获取列表长度
    """
    # TODO: 实现列表操作
    pass


# 练习4：字符串处理函数
def palindrome_check(s):
    """
    检查一个字符串是否为回文（忽略大小写和空格）
    示例：'A man a plan a canal Panama' 是回文
    """
    # TODO: 实现回文检查逻辑
    pass


# 练习5：条件判断和循环
def fizz_buzz(n):
    """
    实现FizzBuzz游戏逻辑：
    - 如果数字能被3整除，返回"Fizz"
    - 如果数字能被5整除，返回"Buzz"  
    - 如果数字能同时被3和5整除，返回"FizzBuzz"
    - 否则返回数字本身
    """
    # TODO: 实现FizzBuzz逻辑
    pass


# 测试用例
if __name__ == "__main__":
    # 测试加法函数
    print("测试加法:")
    print(add(3, 5))  # 应该输出 8
    print(add(-2, 7))  # 应该输出 5

    # 测试减法函数
    print("\n测试减法:")
    print(subtract(10, 3))  # 应该输出 7
    print(subtract(5, 8))  # 应该输出 -3

    # 测试乘法函数
    print("\n测试乘法:")
    print(multiply(4, 6))  # 应该输出 24
    print(multiply(-3, 5))  # 应该输出 -15

    # 测试除法函数
    print("\n测试除法:")
    print(divide(10, 2))  # 应该输出 5.0
    print(divide(7, 0))  # 应该处理除零错误

    # 测试数字分类函数
    print("\n测试数字分类:")
    print(number_category(5))  # 应该输出 "positive odd"
    print(number_category(-4))  # 应该输出 "negative even"
    print(number_category(0))  # 应该输出 "zero"

    # 测试回文检查
    print("\n测试回文检查:")
    print(palindrome_check("A man a plan a canal Panama"))  # 应该输出 True
    print(palindrome_check("hello"))  # 应该输出 False

    # 测试FizzBuzz
    print("\n测试FizzBuzz:")
    for i in range(1, 16):
        print(fizz_buzz(i), end=" ")
    print()
