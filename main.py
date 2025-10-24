def isOdd(value):
    """
    判断输入是否为奇整数
    参数:
    value - 任意类型的输入值
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    if isinstance(value, int):
        return value % 2 == 1
    else:
        return False

# 提示用户输入数字
user_input = input("请输入一个数字：")

# 尝试将输入转换为整数
try:
    num = int(user_input)
    # 调用函数并输出结果
    print(isOdd(num))
except ValueError:
    # 如果输入无法转换为整数，提示错误
    print("输入的不是有效的整数！")
