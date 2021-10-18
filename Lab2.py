import functools, time

# Реализация декоратора для кэширования результата вызова функции
def cacheDecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count +=1
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    wrapper.count = 0
    return wrapper

# Задание 1. Является ли число палиндромом
def isPalindrom(x, part = 0):
    if x == 0:
        return part
    return isPalindrom(x // 10, part * 10 + x % 10)

# Задание 2. Сортировка списка по остатку от деления (2, 3, 5)
def oneIntoThree(l):
    l1 = []
    l2 = []
    l3 = []
    for i in l:
        if (i % 2 == 0):
            l1.append(i)
        if (i % 3 == 0):
            l2.append(i)
        if (i % 5 == 0):
            l3.append(i)
    return l1, l2, l3

# Задание 3. Переворачиватель чисел
def reversedNum(x, part = 0, fl = False):
    if x >= 0:
        if x == 0:
            if fl == True:
                part = part * (-1)
            return part
        return reversedNum(x // 10, part * 10 + x % 10, fl)
    else:
        fl = True
        x = x * (-1)
        return reversedNum(x // 10, part * 10 + x % 10, fl)

# Задание 4. Нахождение корня n-ой степени по методу Ньютона (+ применение декоратора)
@cacheDecorator
def rootNewton(x, n):
    root = x / n
    temp = x
    while abs(root - temp) >= 0.001:
        temp = x
        for i in range(1, n):
            temp = temp / root
        root = 0.5 * (temp + root)
    return round(root, 3)

# Задание 5. Является ли число простым
def isPrime(x):
    j = 2
    while x % j != 0:
        j += 1
    return j == x

# Функция для выбора различных функций
def chooseFunc(inp):
    if (inp == 0):
        return
    elif (inp == 1):
        x = int(input("Input a number: "))
        if isPalindrom(x) == x:
            print("It's a palindrom!")
        else:
            print("It isn't a palindrom!")
    elif (inp == 2):
        l = []
        for i in input("Input list of numbers: ").split():
            l.append(int(i))
        func = oneIntoThree(l)
        for i in func:
            print(i)
    elif (inp == 3):
        x = int(input("Input a number: "))
        print("Reversed number: " + str(reversedNum(x)))
    elif (inp == 4):
        x = int(input("Input a number: "))
        n = int(input("Input n: "))
        # Код для определения времени выполнения функции
        start = time.perf_counter()
        print("Result: ", rootNewton(x, n))
        print('Time run: ', time.perf_counter() - start)
        print("Count: ", rootNewton.count)
    elif (inp == 5):
        x = int(input("Input a number: "))
        if (x >= 0) and (x <= 100000):
            if isPrime(x):
                print("It's a prime number!")
            else:
                print("It isn't a prime number!")
        else:
            print("Number is less than 0 or greater than 100000!")

# Выбор функций
inp = 1
while inp != 0:
    inp = int(input("\nChoose task:\n0. Exit\n1. Is number a palindrom?\n2. Sort list of numbers.\n3. Reverse number.\n4. Calculate n square root. (Decorator)\n5. Is number prime?\n"))
    chooseFunc(inp)