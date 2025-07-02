## Question 1
print("Question 1 Integer Muplication")
def integeraddition(integer1, integer2):
    if integer2 == 1:
        return integer1
    else:
        return integer1 + integeraddition(integer1, integer2-1)

print(integeraddition(int(input("What is your first number? ")), int(input("What is your second number? ")) ))

print("\n")

## Question 2
print("Question 2 Exponentiation")
def raising(a: int, b: int):
    if b == 0:
        return 1
    else:
        return a * raising(a, b - 1)

print(raising(int(input("What is your base? ")), int(input("expo? ")) ))

print("\n")

## Question 3
print("Question 3 Printing from top to bottom")
def printint(n: int):
    if n == 0:
        return 0
    else:
        print(n)
        return printint(n - 1)

print(printint(int(input("What is your top? "))))

print("\n")

## Question 4
print("Question 4 Printing from bottom to top")
def printint2(n: int, i = 0):
    if n == i:
        return n
    else:
        print(i)
        return printint2(n, i + 1)

print(printint2(int(input("How far do you want to go?" )), 0))

print("\n")

## Question 5
print("Question 5 String Reversal")
def reversetext(book: str, currentposition: int):
    len(book)
    if currentposition == len(book)-1:
        return book[currentposition]
    else:
        return reversetext(book, currentposition + 1) + book[currentposition]

print(reversetext(input("What is your book? "), 0))

print("\n")

## Question 6
print("Question 6 Prime Check")
def prime(xas: int, di = None):
    if xas < 1:
        return False

    if di is None:
        di = xas - 1

    if di == 1:
        return True

    if xas % di == 0:
        return False
    return prime(xas, di - 1)

print(f"Prime: {prime(int(input("What natural number are you testing for a prime nature?: ")))}")

print("\n")

print("Question 7 Fibonacci series")
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(7))

print("\n")

from functools import lru_cache

@lru_cache(maxsize=1000)
def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 50
TowerOfHanoi(n, 'A', 'B', 'C')
