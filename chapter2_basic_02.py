"""
在 Python 中，% 运算符主要有两个用途：

    取模（求余数）运算（在数值计算中使用）
    字符串格式化（在格式化字符串中使用）

在 Python 中，== 是相等运算符（equality operator），用于比较两个对象的值是否相等。
如果两个对象的值相等，则返回 True，否则返回 False。

"""

# 定义列表并赋值变量
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 定义空列表赋值变量
even = []
# 使用for循环遍历
for number in numbers:
    # 判断每次取出的数除以2以后的余数是否为0（不为0则为奇数）
    if number % 2 == 0:
        # 将偶数追加下入列表
        even.append(number)

print(even)
