# coding:utf-8
'''
2014-1-19
笨方法学python习题4
变量(varibale)和命名
'''

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers  = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "we can transport", carpool_capacity,"people today."
print "We have", passengers, "to carpll today."
print "We need to put about ",average_passengers_per_car,"in each car."

'''
运行结果正常
总结：主要注意print语句中逗号的用法，连接后面的变量和字符串。
实际打印出来的效果是逗号变成空格并连接后面的变量和字符串。

'''