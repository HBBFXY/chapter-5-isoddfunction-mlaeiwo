def isOdd(value):
    print(f"开始判断输入值：{value}，类型为：{type(value)}")
    # 首先判断是否为整数类型
    if isinstance(value, int):
        print(f"{value} 是整数类型，继续判断奇偶性")
        # 再判断是否为奇数（奇数对 2 取余结果不为 0）
        is_odd = value % 2 != 0
        print(f"{value} 除以 2 的余数为 {value % 2}，{'是' if is_odd else '不是'}奇数")
        return is_odd
    else:
        print(f"{value} 不是整数类型，直接返回 False")
        return False

# 获取用户输入
user_input = input("请输入一个数字：")

try:
    # 尝试将输入的字符串转换为整数
    num = int(user_input)
    print(f"用户输入的数字为：{num}")
    # 调用函数并打印结果
    result = isOdd(num)
    print(f"最终结果：{result}")
except ValueError:
    # 如果输入无法转换为整数，提示错误并调用函数（此时函数会直接返回 False）
    print(f"输入的 '{user_input}' 不是有效的整数！")
    result = isOdd(user_input)
    print(f"最终结果：{result}")
