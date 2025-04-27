# 自定义排序示例

# 1. 使用sorted()函数的key参数
students = [
    {'name': '张三', 'score': 85},
    {'name': '李四', 'score': 92},
    {'name': '王五', 'score': 78},
    {'name': '赵六', 'score': 95}
]

# 按分数降序排序
sorted_by_score = sorted(students, key=lambda x: x['score'], reverse=True)
print("按分数降序排序:")
for student in sorted_by_score:
    print(f"{student['name']}: {student['score']}")

# 2. 使用自定义比较函数
from functools import cmp_to_key

def compare_students(a, b):
    # 先按分数降序，分数相同则按名字升序
    if a['score'] != b['score']:
        return b['score'] - a['score']
    return 1 if a['name'] > b['name'] else -1

sorted_students = sorted(students, key=cmp_to_key(compare_students))
print("\n使用自定义比较函数排序:")
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")

# 3. 对复杂对象进行排序
class Student:
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age
    
    def __repr__(self):
        return f"Student({self.name}, {self.score}, {self.age})"

student_objects = [
    Student('张三', 85, 20),
    Student('李四', 92, 19),
    Student('王五', 78, 21),
    Student('赵六', 95, 20)
]

# 按年龄升序，年龄相同则按分数降序
sorted_objects = sorted(student_objects, key=lambda x: (x.age, -x.score))
print("\n对复杂对象排序:")
for student in sorted_objects:
    print(student) 