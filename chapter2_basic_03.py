
def euclidean_division(dividend, divisor):
    """
    执行欧几里得除法。

    参数:
    dividend (int): 被除数。
    divisor (int): 除数。

    返回:
    tuple: 包含商和余数的元组。
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# 对3和2执行欧几里得除法，并打印商和余数
t = euclidean_division(3, 2)
print(t[0])
print(t[1])

# 对42和4执行欧几里得除法，并打印商和余数
q, r = euclidean_division(42, 4)
print(q)
print(r)

