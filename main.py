def isOdd(value):
    """
    判断输入是否为整数且为奇数
    参数:
    value - 任意类型的输入值
    返回:
    bool - 是整数且为奇数返回 True，否则返回 False
    """
    # 先判断是否为整数
    if isinstance(value, int):
        # 再判断是否为奇数（奇数对 2 取余为 1）
        return value % 2 == 1
    # 非整数直接返回 False
    return False

# 测试用例
print(isOdd(3))    # 整数且奇数 → True
print(isOdd(4))    # 整数但偶数 → False
print(isOdd(3.5))  # 浮点数 → False
print(isOdd("a"))  # 字符串 → False
