# 字符串处理示例

# 1. 基本字符串操作
text = "  Python字符串处理示例  "
print("原始字符串:", text)

# 去除空格
print("\n1. 去除空格:")
print("去除两端空格:", text.strip())
print("去除左端空格:", text.lstrip())
print("去除右端空格:", text.rstrip())

# 2. 字符串大小写转换
text = "Hello World"
print("\n2. 大小写转换:")
print("转换为大写:", text.upper())
print("转换为小写:", text.lower())
print("首字母大写:", text.capitalize())
print("每个单词首字母大写:", text.title())

# 3. 字符串查找和替换
text = "Python是一门非常强大的编程语言，Python简单易学"
print("\n3. 字符串查找和替换:")
print("查找'Python'的位置:", text.find("Python"))
print("从右侧查找'Python'的位置:", text.rfind("Python"))
print("统计'Python'出现的次数:", text.count("Python"))
print("替换'Python'为'Java':", text.replace("Python", "Java"))

# 4. 字符串分割和连接
text = "apple,banana,orange,grape"
print("\n4. 字符串分割和连接:")
fruits = text.split(",")
print("分割后的列表:", fruits)
print("使用'-'重新连接:", "-".join(fruits))

# 5. 字符串格式化
name = "张三"
age = 25
score = 95.5
print("\n5. 字符串格式化:")
print("使用f-string:", f"姓名：{name}，年龄：{age}，分数：{score}")
print("使用format方法:", "姓名：{}，年龄：{}，分数：{}".format(name, age, score))
print("使用%格式化:", "姓名：%s，年龄：%d，分数：%.1f" % (name, age, score))

# 6. 字符串检查
text = "Python123"
print("\n6. 字符串检查:")
print("是否全为字母:", text.isalpha())
print("是否全为数字:", text.isdigit())
print("是否全为字母或数字:", text.isalnum())
print("是否全为小写:", text.islower())
print("是否全为大写:", text.isupper())

# 7. 字符串切片
text = "Hello, World!"
print("\n7. 字符串切片:")
print("获取前5个字符:", text[:5])
print("获取后6个字符:", text[-6:])
print("获取第2到第5个字符:", text[1:5])
print("每隔2个字符取一个:", text[::2])

# 8. 字符串编码和解码
text = "你好，世界！"
print("\n8. 字符串编码和解码:")
encoded = text.encode('utf-8')
print("UTF-8编码:", encoded)
decoded = encoded.decode('utf-8')
print("UTF-8解码:", decoded) 