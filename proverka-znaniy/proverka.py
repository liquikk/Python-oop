from memory_profiler import memory_usage
import time
from math import sqrt

def n1(a,b,c):
    startTime = time.time()
    q=0
    q=b
    b=c
    c=a
    a=q
    endTime = time.time()
    totalTime = endTime - startTime
    print(f"затраченное время {totalTime} sec")
    print(memory_usage(),'Мбайт')
    return a, b, c

def n2():
    req=False
    n = int(input('введите n\n'))
    mas = [None] * n
    t=0
    sum=0
    while req==False:
        print(f"введите {n} чисел")
        for i in range(n):
            a = input()
            mas[i]=a
        try:
            for i in range(n):
                mas[i]=int(mas[i])
        except ValueError:
            print('*Ошибка* введите числа снова')
            continue
        for i in range(n):
            if type(mas[i]) == int:
                t=1
            else:
                t=0
        if t == 1:
            req=True
    for i in range(n):
        sum+=mas[i]
    return sum

def n3(x):
    startTime = time.time()
    if x<0 or x>100:
        print("введено неправильное число")
        exit
    else:
        endTime = time.time()
        totalTime = endTime - startTime
        print(f"затраченное время {totalTime} sec")    
        print(memory_usage(),'Мбайт')
        return x*x*x*x*x

def n4(n):
    if n<0 or n>250:
        print("введено неправильное число")
        exit
    else:
        if sqrt(5*(n**2)-4)%1 == 0 or sqrt(5*(n**2)+4)%1 == 0:
            return True
        else:
            return False

def n6(n):
    chet = 0
    nechet = 0
    sum_chet = 0
    sum_nechet = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            chet+=1
            sum_chet+=i
        else:
            nechet+=1
            sum_nechet+=i
    print(f"кол-во чет: {chet} кол-во нечет {nechet}")
    print(f"сумма чет: {sum_chet} сумма нечет {sum_nechet}")

def n7(): #я не считал само проверяемое число за делитель
    vvod=False
    while vvod==False:
        n=int(input('введите n'))
        if n>=250:
            print("введено неправильное число")
            continue
        else:
            vvod=True
    startTime = time.time()
    for i in range(1,n+1):
        d=0
        for j in range(1,i):
            if i%j==0:
                d+=1
        print(i, d)
    endTime = time.time()
    totalTime = endTime - startTime
    print(f"затраченное время {totalTime} sec")    

def n12():
    a = input("введите массив\n")
    numbers = map(int, a.split())
    b = (list(numbers))
    print(b[::-1])
