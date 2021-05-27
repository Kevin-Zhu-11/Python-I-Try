# 竭尽所能去尝试吧
# Come on
# print 520
money=1000
s=int(input('请输入取款金额'))
if money>=s:    #条件表达式
    money=money-s
    print('取款成功,余额为',money)
else:
    print('余额不足')



a=int(input('请输入一个整数'))
if a%2==0:
    print(a,'是偶数')
else:
    print(a,'是奇数')