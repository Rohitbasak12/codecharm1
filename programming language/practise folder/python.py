def my_abs(value):
    """Returns absolute value without using abs function"""
    if value <= 0:
        return value * -1
    return value * 1
a = input()
res = my_abs(a)
print(String(res))