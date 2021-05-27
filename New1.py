# 竭尽所能去尝试吧
# Come on
# print 520
s = 'Hello, Runoob'
str(s)
'Hello, Runoob'
repr(s)
"'Hello, Runoob'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)
x 的值为： 32.5,  y 的值为：40000
...
#  repr() 函数可以转义字符串中的特殊字符
...
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)
'hello, runoob\n'
# repr() 的参数可以是 Python 的任何对象
...
repr((x, y, ('Google', 'Runoob')))
"(32.5, 40000, ('Google', 'Runoob'))"