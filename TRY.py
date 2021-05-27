# 竭尽所能去尝试吧
# Come on
# print 520

#执行下面的程序在按回车键后就会等待用户输入：
input('\n\n按下enter后退出')#

#以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。



#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
#使用脚本执行以上代码，输出结果为：runoob
#使用交互式命令行执行，输出结果为：runoob     7  此处的 7 表示字符数

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()


