def multiple(func):
    def inner(*args, **kwargs):
        x = args[0]
        y = args[1]
        return x * y
    return inner

def plus(func):
    def inner(*args, **kwargs):
        x = args[0]
        y = args[1]
        return x + y
    return inner

def minus(func):
    def inner(*args, **kwargs):
        x = args[0]
        y = args[1]
        return x - y
    return inner

def divine(func):
    def inner(*args, **kwargs):
        x = args[0]
        y = args[1]
        return x / y
    return inner

@multiple
def num(x, y):
    return x, y

print(num(1000, 10))

# def cache(func):
#     cached_results = {}
#     def wrapper(*args):
#         if args in cached_results:
#             return cached_results[args]
#         result = func(*args)
#         cached_results[args] = result
#         return result
#     return wrapper

# @cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# fibo = fibonacci(10)
# print(fibo)