# 测试原始字符串和普通字符串的区别

print("=== 路径字符串测试 ===")

# 1. 普通字符串
normal_path = 'tmp\examples\lena512.raw'
print(f"普通字符串: {normal_path}")
print(f"长度: {len(normal_path)}")

# 2. 原始字符串
raw_path = r'tmp\examples\lena512.raw'
print(f"原始字符串: {raw_path}")
print(f"长度: {len(raw_path)}")

# 3. 转义字符串
escaped_path = 'tmp\\examples\\lena512.raw'
print(f"转义字符串: {escaped_path}")
print(f"长度: {len(escaped_path)}")

print("\n=== 特殊字符测试 ===")

# 测试特殊字符
test_string1 = 'Hello\nWorld'  # \n 被解释为换行符
print(f"普通字符串: '{test_string1}'")

test_string2 = r'Hello\nWorld'  # \n 被当作普通字符
print(f"原始字符串: '{test_string2}'")

print("\n=== 文件路径测试 ===")

# 模拟文件路径
paths = [
    'C:\new\test.txt',      # 普通字符串 - 有问题
    r'C:\new\test.txt',     # 原始字符串 - 正确
    'C:\\new\\test.txt',    # 转义字符串 - 正确
    'C:/new/test.txt'       # 正斜杠 - 正确
]

for i, path in enumerate(paths, 1):
    print(f"{i}. {path}")
