# 编程判断一个人是否是微博活跃用户
x = int(input("最近三天登录次数是？"))
y = int(input("最近三天发微博数是？"))
print("该用户是",end="")   #end=""是什么意思?表示的是以换行符结尾
# 判断是否是非常活跃用户
if x > 20 or y > 10 :
	print("非常活跃用户")
# 判断是否是活跃用户
elif 10 <= x < 20 or 5 <= y < 10:
	print("活跃用户")
# 判断是否是消极用户
elif x < 3 and y <= 1:
	print("消极用户")
# 判断是否是普通用户
else:
	print("普通用户")