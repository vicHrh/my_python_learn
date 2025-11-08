# 输入
# input_str = input("请输入一个字符串：")
# print("您刚才输入的数据类型为:",type(input_str))
# print("您输入的字符串为:",input_str)

print("hello Python")
print("hello","Python")

print("hello\\n 结尾",end="\n")

print("hello\\n 结尾",end="")
print("world")

int1 = 10
float1 = 10.12345
# str1 = "int1 = %d,float1 = %f" %(int1,float1)
# print(str1)
bool1 = True

str2 = "int1 = {},float1 = {},bool1 = {}".format(int1,float1,bool1)
print(str2)


str3 = "{:0<20,.2f}".format(123456789.123456789)
print(str3)