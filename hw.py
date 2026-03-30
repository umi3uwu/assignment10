import time
import functools
from functools import reduce

def operation(func, x: int, y: int) -> int:
    return func(x, y)

def my_map(func, my_list: list) -> list:
    res = []
    for i in my_list:
        res.append(func(i))
    return res

def filter_even_numbers(numbers: list) -> list:
    return list(filter(lambda x: x % 2 != 0, numbers))

def recursive_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

def timeit_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {duration:.4f} сек.")
        return result
    return wrapper

def compose(*funcs):
    def inner(x):
        for f in funcs:
            x = f(x)
        return x
    return inner

def partial(func, *args):
    def wrapper(*new_args):
        return func(*args, *new_args)
    return wrapper

def factorial_reduce(n: int) -> int:
    if n == 0: return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def my_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
    return value

def sort_by_last_letter(words: list) -> list:
    return sorted(words, key=lambda x: x[-1])

def recursive_reverse(my_list: list) -> list:
    if len(my_list) <= 1:
        return my_list
    return [my_list[-1]] + recursive_reverse(my_list[:-1])

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"'{func.__name__}' was called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def find_max(numbers: list) -> int:
    return reduce(lambda x, y: x if x > y else y, numbers)

def remove_elements(my_list: list, element):
    return list(filter(lambda x: x != element, my_list))

def repeat(n: int):
    return lambda s: s * n

def recursive_sum(my_list: list) -> int:
    if not my_list:
        return 0
    return my_list[0] + recursive_sum(my_list[1:])

def add_two_lists(list1: list, list2: list) -> list:
    return list(map(lambda x, y: x + y, list1, list2))