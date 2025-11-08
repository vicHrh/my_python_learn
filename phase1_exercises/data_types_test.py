"""
第一阶段练习：Python数据类型操作
目标：熟悉Python各种数据类型的特点和操作方法
"""

# 练习1：列表操作
def list_manipulation():
    """
    创建一个函数演示列表的各种操作：
    1. 创建一个包含至少5个元素的列表
    2. 在末尾添加新元素
    3. 在指定位置插入元素
    4. 删除指定元素
    5. 对列表进行排序
    6. 反转列表
    7. 使用列表推导式创建新列表
    """
    # TODO: 实现列表操作
    my_list = []
    return my_list

# 练习2：字典操作
def dictionary_operations():
    """
    创建一个函数演示字典的各种操作：
    1. 创建一个字典存储个人信息（姓名、年龄、职业等）
    2. 添加新的键值对
    3. 修改现有值
    4. 删除键值对
    5. 遍历字典的键和值
    6. 检查某个键是否存在
    """
    # TODO: 实现字典操作
    my_dict = {}
    return my_dict

# 练习3：元组操作
def tuple_operations():
    """
    创建一个函数演示元组的特点：
    1. 创建元组
    2. 访问元组元素
    3. 元组拆包
    4. 展示元组不可变性
    """
    # TODO: 实现元组操作
    my_tuple = ()
    return my_tuple

# 练习4：集合操作
def set_operations():
    """
    创建一个函数演示集合的操作：
    1. 创建两个集合
    2. 执行交集、并集、差集操作
    3. 添加和删除元素
    4. 检查子集关系
    """
    # TODO: 实现集合操作
    set1 = set()
    set2 = set()
    return set1, set2

# 练习5：字符串操作
def string_operations():
    """
    创建一个函数演示Python强大的字符串处理功能：
    1. 字符串格式化（多种方法）
    2. 字符串分割和连接
    3. 大小写转换
    4. 去除空白字符
    5. 查找和替换
    """
    # TODO: 实现字符串操作
    test_string = "  Hello, World! Welcome to Python.  "
    return test_string

# 测试代码
if __name__ == "__main__":
    print("练习1: 列表操作")
    result_list = list_manipulation()
    print(f"结果: {result_list}")
    
    print("\n练习2: 字典操作")
    result_dict = dictionary_operations()
    print(f"结果: {result_dict}")
    
    print("\n练习3: 元组操作")
    result_tuple = tuple_operations()
    print(f"结果: {result_tuple}")
    
    print("\n练习4: 集合操作")
    set1, set2 = set_operations()
    print(f"集合1: {set1}")
    print(f"集合2: {set2}")
    
    print("\n练习5: 字符串操作")
    result_string = string_operations()
    print(f"结果: '{result_string}'")