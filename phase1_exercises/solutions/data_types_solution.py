"""
第一阶段练习参考答案：Python数据类型操作
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
    # 创建包含5个元素的列表
    my_list = [3, 1, 4, 1, 5]
    
    # 在末尾添加新元素
    my_list.append(9)
    
    # 在指定位置插入元素
    my_list.insert(2, 2)
    
    # 删除指定元素（删除值为1的第一个元素）
    my_list.remove(1)
    
    # 对列表进行排序
    my_list.sort()
    
    # 反转列表
    my_list.reverse()
    
    # 使用列表推导式创建新列表（每个元素的平方）
    squared_list = [x**2 for x in my_list]
    
    return my_list, squared_list

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
    # 创建字典存储个人信息
    my_dict = {
        "name": "张三",
        "age": 25,
        "occupation": "工程师"
    }
    
    # 添加新的键值对
    my_dict["city"] = "北京"
    
    # 修改现有值
    my_dict["age"] = 26
    
    # 删除键值对
    del my_dict["occupation"]
    
    # 遍历字典的键和值
    print("字典内容:")
    for key, value in my_dict.items():
        print(f"  {key}: {value}")
    
    # 检查某个键是否存在
    has_email = "email" in my_dict
    
    return my_dict, has_email

# 练习3：元组操作
def tuple_operations():
    """
    创建一个函数演示元组的特点：
    1. 创建元组
    2. 访问元组元素
    3. 元组拆包
    4. 展示元组不可变性
    """
    # 创建元组
    my_tuple = (1, 2, 3, "Python", 3.14)
    
    # 访问元组元素
    first_element = my_tuple[0]
    last_element = my_tuple[-1]
    
    # 元组拆包
    a, b, c, language, pi = my_tuple
    
    # 展示元组不可变性（注释掉的代码会报错）
    # my_tuple[0] = 10  # 这行会引发TypeError
    
    return my_tuple, first_element, last_element, language, pi

# 练习4：集合操作
def set_operations():
    """
    创建一个函数演示集合的操作：
    1. 创建两个集合
    2. 执行交集、并集、差集操作
    3. 添加和删除元素
    4. 检查子集关系
    """
    # 创建两个集合
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    # 执行交集、并集、差集操作
    intersection = set1 & set2  # 或者 set1.intersection(set2)
    union = set1 | set2         # 或者 set1.union(set2)
    difference = set1 - set2    # 或者 set1.difference(set2)
    
    # 添加和删除元素
    set1.add(6)
    set1.discard(1)  # 删除元素，如果不存在也不会报错
    
    # 检查子集关系
    is_subset = {2, 3}.issubset(set1)
    
    return set1, set2, intersection, union, difference, is_subset

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
    # 原始字符串
    test_string = "  Hello, World! Welcome to Python.  "
    
    # 去除空白字符
    stripped = test_string.strip()
    
    # 大小写转换
    upper_case = stripped.upper()
    lower_case = stripped.lower()
    title_case = stripped.title()
    
    # 字符串分割和连接
    words = stripped.split()  # 默认按空白字符分割
    joined = "-".join(words)
    
    # 查找和替换
    position = stripped.find("World")
    replaced = stripped.replace("World", "Python")
    
    # 字符串格式化
    name, age = "李四", 30
    formatted1 = f"姓名: {name}, 年龄: {age}"  # f-string (推荐)
    formatted2 = "姓名: {}, 年龄: {}".format(name, age)  # format方法
    formatted3 = "姓名: %s, 年龄: %d" % (name, age)  # % 格式化
    
    return {
        "原始字符串": test_string,
        "去除空白后": stripped,
        "大写": upper_case,
        "小写": lower_case,
        "标题格式": title_case,
        "分割后": words,
        "连接后": joined,
        "查找位置": position,
        "替换后": replaced,
        "f-string格式化": formatted1,
        "format格式化": formatted2,
        "百分号格式化": formatted3
    }

# 测试代码
if __name__ == "__main__":
    print("练习1: 列表操作")
    original_list, squared_list = list_manipulation()
    print(f"原始列表操作后: {original_list}")
    print(f"平方列表: {squared_list}")
    
    print("\n练习2: 字典操作")
    result_dict, has_email = dictionary_operations()
    print(f"最终字典: {result_dict}")
    print(f"是否有email键: {has_email}")
    
    print("\n练习3: 元组操作")
    tuple_result, first, last, lang, pi_value = tuple_operations()
    print(f"元组: {tuple_result}")
    print(f"第一个元素: {first}, 最后一个元素: {last}")
    print(f"解包得到语言: {lang}, π值: {pi_value}")
    
    print("\n练习4: 集合操作")
    s1, s2, inter, uni, diff, subset = set_operations()
    print(f"集合1: {s1}")
    print(f"集合2: {s2}")
    print(f"交集: {inter}")
    print(f"并集: {uni}")
    print(f"差集: {diff}")
    print(f"{2, 3}是集合1的子集: {subset}")
    
    print("\n练习5: 字符串操作")
    string_results = string_operations()
    for description, result in string_results.items():
        print(f"{description}: '{result}'")