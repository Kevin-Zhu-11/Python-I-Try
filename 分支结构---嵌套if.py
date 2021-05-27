# 竭尽所能去尝试吧
# Come on
# print 520
'''s=input('是否是会员')
if '是'==s:
    a=int(input('请输入消费金额'))
    if a>=200:
        print('消费金额为：',a*0.8)
    else:
        print('消费金额为：',a*0.9)
else:
    b=int(input('请输入消费金额'))
    print('消费金额为：',b*0.9)'''


s=input('是否是会员')
a=int(input('请输入消费金额'))
if '是'==s:
    if a >= 200:
        print('消费金额为：', a * 0.8)
    else:
        print('消费金额为：', a * 0.9)
else:
    print('消费金额为：', a * 0.9)


#这应该是我第一个看到问题建出来的模型






