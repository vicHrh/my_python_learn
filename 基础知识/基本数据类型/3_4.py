num1 = True
num2 = 10

print(type(num1))
print(type(num2))

print(type(num1) == type(num2))
print(isinstance(num1, int))
print(isinstance(num2, int))

print(isinstance(num1, bool))
print(isinstance(num2, bool))

# String 类型的
print("""########### String ###########""")

str1 = '你好中国'
print(str1)
print(type(str1))

byte1 = str1.encode(encoding='utf-8')
print(byte1)

print(type(byte1))

str2 = byte1.decode(encoding='utf-8')
print(str2)


