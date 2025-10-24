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
user_input = input("请输入一个数字：")
