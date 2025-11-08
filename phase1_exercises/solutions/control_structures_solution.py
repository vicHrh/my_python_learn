"""
第一阶段练习参考答案：控制结构
"""

# 练习1：条件语句
def grade_evaluation(score):
    """
    根据分数评定等级：
    - 90分及以上：优秀(A)
    - 80-89分：良好(B)
    - 70-79分：中等(C)
    - 60-69分：及格(D)
    - 60分以下：不及格(F)
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 练习2：简单循环
def sum_up_to_n(n):
    """
    计算从1加到n的总和
    要求使用循环实现（不能使用公式）
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 练习3：嵌套循环
def multiplication_table():
    """
    打印九九乘法表
    格式要求：
    1x1=1
    1x2=2 2x2=4
    1x3=3 2x3=6 3x3=9
    ...
    """
    for i in range(1, 10):
        line = ""
        for j in range(1, i + 1):
            line += f"{j}x{i}={i*j} "
        print(line.strip())

# 练习4：列表推导式
def list_comprehensions_practice():
    """
    使用列表推导式完成以下任务：
    1. 创建包含0到19所有偶数的列表
    2. 创建包含1到10所有数字的平方的列表
    3. 从列表['apple', 'banana', 'cherry', 'date']中筛选出长度大于5的字符串
    4. 将列表['Hello', 'World', 'Python']中所有字符串转换为小写
    """
    # 0到19的所有偶数
    evens = [x for x in range(20) if x % 2 == 0]
    
    # 1到10所有数字的平方
    squares = [x**2 for x in range(1, 11)]
    
    # 长度大于5的字符串
    long_strings = [s for s in ['apple', 'banana', 'cherry', 'date'] if len(s) > 5]
    
    # 转换为小写的字符串
    lowercase = [s.lower() for s in ['Hello', 'World', 'Python']]
    
    return evens, squares, long_strings, lowercase

# 练习5：综合应用 - 猜数字游戏
def guess_number_game():
    """
    实现一个猜数字游戏：
    1. 随机生成一个1-100之间的数字
    2. 用户输入猜测的数字
    3. 根据用户输入给出提示（太大/太小/正确）
    4. 记录猜测次数
    5. 猜对后显示结果
    """
    import random
    
    # 生成随机数
    target = random.randint(1, 100)
    
    # 初始化变量
    guess = None
    attempts = 0
    
    # 简化版本 - 使用预设值进行演示
    test_values = [50, 75, 87, 93, 96, 98]  # 模拟用户输入
    test_index = 0
    
    # 游戏主循环
    while guess != target and test_index < len(test_values):
        # 获取"用户"输入
        guess = test_values[test_index]
        test_index += 1
        attempts += 1
        
        # 比较并给出提示
        if guess < target:
            print(f"{guess} 太小了!")
        elif guess > target:
            print(f"{guess} 太大了!")
        else:
            print(f"恭喜你，猜对了! 目标数字就是 {target}")
            break
    
    # 防止无限循环的退出条件
    if guess != target:
        print(f"游戏结束! 目标数字是 {target}")
    
    return target, attempts

# 测试代码
if __name__ == "__main__":
    print("练习1: 条件语句")
    print(f"分数85的等级: {grade_evaluation(85)}")
    print(f"分数95的等级: {grade_evaluation(95)}")
    print(f"分数55的等级: {grade_evaluation(55)}")
    
    print("\n练习2: 简单循环")
    print(f"1加到10的和: {sum_up_to_n(10)}")
    print(f"1加到100的和: {sum_up_to_n(100)}")
    
    print("\n练习3: 嵌套循环 - 九九乘法表")
    multiplication_table()
    
    print("\n练习4: 列表推导式")
    evens, squares, long_strings, lowercase = list_comprehensions_practice()
    print(f"0到19的偶数: {evens}")
    print(f"1到10的平方: {squares}")
    print(f"长度大于5的字符串: {long_strings}")
    print(f"小写字符串: {lowercase}")
    
    print("\n练习5: 猜数字游戏")
    target, attempts = guess_number_game()
    print(f"目标数字: {target}, 尝试次数: {attempts}")