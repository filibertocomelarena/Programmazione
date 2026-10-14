'''Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
 The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:


Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34'''

def fibonacci(n): #fib ricorsivo
    if n ==1:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(n)

print(fibonacci(9))



