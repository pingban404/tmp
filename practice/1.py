from encodings import utf_8
from itertools import count
import random
from re import L
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)  # 执行被装饰的函数
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} Elapsed time: {elapsed_time:.6f} seconds")
        return result  # 返回原函数的结果
    return wrapper
#输入的数是否为素数

def is_ss(i):
    is_true=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_true=False
            break
    return(is_true)

#斐波那契数列
def fbnc():
    a,b=0,1
    for _ in range(20):
        a,b=b,a+b
        print(a)

#水仙花
def shuixianhua():
    for i in range(100,999+1):
        i1=i%10
        i2=i//10%10
        i3=i//100
        if i==i3**3+i2**3+i1**3:
            print(i)
        
#百钱百鸡
def jiji():
    jhigh=5
    jmid=3
    jlow=1/3
    for x in range(0,100//jhigh+1):
        for y in range(0,100//jmid+1):
            for z in range(0,int(100/jlow)+1):
                if x+z+y<=100:
                    print(f'公鸡={x:}，母鸡={y:}，小鸡={z:}')
#百钱百鸡pro
# @timer
def jiji1():
    jhigh=5
    jmid=3
    jlow=1/3
    for x in range(0,100//jhigh+1):
        for y in range(0,100//jmid+1):
            z=100-x-y
            if z>=0 and z%3==0 and x+z+y<=100:
                    print(f'公鸡={x:}，母鸡={y:}，小鸡={z:}')


#CRAPS赌博游戏
def craps(mymoney):
    money=int(mymoney)
    dmoney=money
    is_true=True
    while is_true:
        print(f'你的初始资金是:{money:}')
        debt=int(input("请下注:"))


        while True:
                if 0 < debt <= 2*dmoney:
                    break
                else:
                    print(f'你的余额为{money},你的下注超过了你本金的一倍，请重新下注')
                    debt=int(input("请下注:"))
        
        fpoint=random.randrange(1,7)+random.randrange(1,7)
        print(f'投出了{fpoint:}')
        match fpoint:
            case 2|3|12:
                print("庄家胜出！")
                money=money-debt
            case 7|11:
                print("玩家胜出！")
                money=money+debt
            case _ :
                print("未决出胜负！，请进行第二次下注")
                print(f'你的资金是:{money:}')
                debt=int(input("请下注:"))
                while True:
                    if 0 < debt <= 2*dmoney:
                        break
                    else:
                        print(f'你的余额为{money},你的下注超过了你本金的一倍，请重新下注')
                        debt=int(input("请下注:"))
                spoint=random.randrange(1,7)+random.randrange(1,7)
                if spoint==fpoint:
                    print("玩家胜出！")
                    money=money+debt
                else:
                    print("庄家胜出！")
                    money=money-debt

        if money<0:
            print(f'你已经破产,你的余额为{money:}')
            break

@timer
def mylist():
    items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
    print(items[::-1]) 
    items.reverse()
    print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']
# 
@timer
def mylist2():
    nums1 = [35, 12, 97, 64, 55]
    num2=[]
    for num in nums1[::]:
        if num >50:
           nums1.remove(num)
           num2.append(num)
        print('-'*20)
        print(f'nums1={nums1:}')
        print(f'num2={num2:}')

def mylist3():
    item=[[random.randrange(60,101) for _ in range(3)] for _ in range(3)]
    print(item)

def shuangseqiu():
    from rich.console import Console
    from rich.table import Table
    console=Console()
    n=int(input('记号注:'))
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    tables=Table(show_header=True)
    for col_name in ('序号', '红球', '蓝球'):
        tables.add_column(col_name,justify='center')
    

    for i in range(n):
        selected_balls=random.sample(red_balls,6)
        selected_balls.sort()
        
        selected_blue=random.choice(blue_balls)
        tables.add_row(
            str(i+1),
            f'[red]{"-".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
            f'[blue]{selected_blue:0>2d}[/blue]'
        )
    console.print(tables)

def yuanzu():
    import timeit

    print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
    print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
    execution_time = timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000)
    print(f'{execution_time:.3f}秒')


def string1():
    
    s = 'I love you somuch'

    s1=s.split(" ")
    s2=list()
    print(s.encode('utf-8'))
    print(f' '.join(s1))
    for n in s1:
        s2.append(n[::-1])
    print(s2)

def zuhe():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)

    set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
    print(set2)

    set3 = set('hello')
    print(set3)

    set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
    print(set4)

    set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
    print(set5)
    print(f'-'*50)
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    for elem in set1:
        print(elem)

def dictionary():
    stocks = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    s1={key:v for key,v in stocks.items() if v >100}
    print(s1)
    


dictionary()