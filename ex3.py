# coding:utf-8
'''
2014-1-19
笨方法学python习题3
数字和数学计算
'''

'''
常用数学计算符号
+ plus 加号
- minus 减号
/ slash 斜杠
* asterisk 星号
% percent 百分号
< less-than 小于号
> greater-than 大于号
<= less-than-equal 小于等于
>= greater-than-equal 大于等于
'''

print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "Is it ture that 3+2<5-7?"
print 3 + 2 < 5 - 7

print "What is 3+2?", 3 + 2
print "What is 5 -7?", 5 - 7

print "Oh,that's False."
print "How about some more."
print "Is it greater?", 5 > -2
print "Is it greater osr equal?", 5 <= -2
print "Is it less or equal?", 5 <= -2

'''
运行结果正常
总结：< ,> ,<=,>= 表达式返回的是布尔值False和True
其他符号用于数字计算，计算出值出来
运算级别从高到低依次是：括号、指数、乘、除、加、减

'''
