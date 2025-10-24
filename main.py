def isOdd(value):
    """
    判断输入是否为奇整数
    参数:
    value - 任意类型的输入值
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    # 首先检查类型是否为整数
    if isinstance(value, int):
        # 然后检查奇偶性，奇数对 2 取余结果为 1
        return value % 2 == 1
    # 如果不是整数，直接返回 False
    else:
        return False
