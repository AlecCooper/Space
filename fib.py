# Fast calculation of fibonacci numbers using memoization
def fib(n, memoize={0:0, 1:1}):

    if not n in memoize:
        memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)

    return memoize[n]


# Calculate a fibonacci number!
print(fib(100))