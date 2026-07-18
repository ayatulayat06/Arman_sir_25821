# Function to generate Fibonacci series as a list
def generate_fibonacci(n):
    if n <=0:
        return []
    elif n == 1:
        return [0]
 
    fib_series = [0, 1]
    for i in range(2, n):
        next_val = fib_series[-1] + fib_series[-2]
        fib_series.append(next_val)
    return fib_series
print("First 10 Fibonacci numbers:", generate_fibonacci(10))

