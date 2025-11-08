"""
第一阶段练习：控制结构
目标：掌握Python中的条件语句、循环语句以及独特的列表推导式
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
    # TODO: 实现等级评定逻辑
    pass

# 练习2：简单循环
def sum_up_to_n(n):
    """
    计算从1加到n的总和
    要求使用循环实现（不能使用公式）
    """
    # TODO: 实现求和逻辑
    pass

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
    # TODO: 实现九九乘法表打印逻辑
    pass

# 练习4：列表推导式
def list_comprehensions_practice():
    """
    使用列表推导式完成以下任务：
    1. 创建包含0到19所有偶数的列表
    2. 创建包含1到10所有数字的平方的列表
    3. 从列表['apple', 'banana', 'cherry', 'date']中筛选出长度大于5的字符串
    4. 将列表['Hello', 'World', 'Python']中所有字符串转换为小写
    """
    # TODO: 使用列表推导式实现以上功能
    evens = []          # 0到19的所有偶数
    squares = []        # 1到10所有数字的平方
    long_strings = []   # 长度大于5的字符串
    lowercase = []      # 转换为小写的字符串
    
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
    
    注意：此函数可以只写出框架逻辑，完整实现可在学习模块后完成
    """
    # TODO: 实现猜数字游戏逻辑
    import random
    
    # 生成随机数
    target = random.randint(1, 100)
    
    # 初始化变量
    guess = None
    attempts = 0
    
    # 游戏主循环
    while guess != target:
        # 获取用户输入（暂时使用固定值）
        guess = 50  # 示例值，实际应获取用户输入
        attempts += 1
        
        # 比较并给出提示
        # TODO: 实现比较逻辑
        
        # 为了防止无限循环，这里添加退出条件
        if attempts > 10:
            break
    
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