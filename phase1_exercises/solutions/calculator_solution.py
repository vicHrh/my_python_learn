"""
第一阶段练习参考答案：基础语法 - 计算器程序
"""

# 练习1：基础运算函数
def add(a, b):
    """实现加法运算"""
    return a + b

def subtract(a, b):
    """实现减法运算"""
    return a - b

def multiply(a, b):
    """实现乘法运算"""
    return a * b

def divide(a, b):
    """实现除法运算，注意处理除零错误"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

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
    if num == 0:
        category = "zero"
    elif num > 0:
        category = "positive"
    else:
        category = "negative"
    
    if num != 0 and num % 2 == 0:
        category += " even"
    elif num != 0:
        category += " odd"
        
    return category

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
    # 创建空列表
    my_list = []
    
    # 添加元素
    my_list.append("apple")
    my_list.append("banana")
    
    # 插入元素
    my_list.insert(1, "orange")
    
    # 删除元素
    my_list.remove("banana")
    
    # 获取列表长度
    length = len(my_list)
    
    return my_list, length

# 练习4：字符串处理函数
def palindrome_check(s):
    """
    检查一个字符串是否为回文（忽略大小写和空格）
    示例：'A man a plan a canal Panama' 是回文
    """
    # 移除空格并转换为小写
    cleaned = ''.join(s.split()).lower()
    # 检查是否等于其反转
    return cleaned == cleaned[::-1]

# 练习5：条件判断和循环
def fizz_buzz(n):
    """
    实现FizzBuzz游戏逻辑：
    - 如果数字能被3整除，返回"Fizz"
    - 如果数字能被5整除，返回"Buzz"  
    - 如果数字能同时被3和5整除，返回"FizzBuzz"
    - 否则返回数字本身
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

# 测试用例
if __name__ == "__main__":
    # 测试加法函数
    print("测试加法:")
    print(add(3, 5))  # 输出 8
    print(add(-2, 7))  # 输出 5
    
    # 测试减法函数
    print("\n测试减法:")
    print(subtract(10, 3))  # 输出 7
    print(subtract(5, 8))   # 输出 -3
    
    # 测试乘法函数
    print("\n测试乘法:")
    print(multiply(4, 6))   # 输出 24
    print(multiply(-3, 5))  # 输出 -15
    
    # 测试除法函数
    print("\n测试除法:")
    print(divide(10, 2))    # 输出 5.0
    try:
        print(divide(7, 0))     # 处理除零错误
    except ValueError as e:
        print(f"错误: {e}")
    
    # 测试数字分类函数
    print("\n测试数字分类:")
    print(number_category(5))   # 输出 "positive odd"
    print(number_category(-4))  # 输出 "negative even"
    print(number_category(0))   # 输出 "zero"
    
    # 测试回文检查
    print("\n测试回文检查:")
    print(palindrome_check("A man a plan a canal Panama"))  # 输出 True
    print(palindrome_check("hello"))  # 输出 False
    
    # 测试FizzBuzz
    print("\n测试FizzBuzz:")
    for i in range(1, 16):
        print(fizz_buzz(i), end=" ")
    print()
    
    # 测试列表操作
    print("\n测试列表操作:")
    lst, length = list_operations()
    print(f"列表: {lst}, 长度: {length}")