# coding:utf-8
'''
2014-1-19
笨方法学python习题5
更多的变量和打印
'''

my_name = 'Zed A.Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall ." % my_height
print "He's %d pound s heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s epending on the coffee." % my_teeth

# this line is tricky,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)


'''
运行结果正常
总结：了解字符格式化%d, %r, %s  用法
 

'''

