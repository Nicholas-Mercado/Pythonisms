from functools import wraps
from time import time


def exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        un_changed_function_return = func(*args, **kwargs)

        exclamation = un_changed_function_return + "!!!!!"

        return exclamation

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function : {func.__name__!r} finished in {(t2-t):.4f}s")
        return result
    return wrapper

@exclamation
@timer
def say(txt):
    return txt

@timer
def long_function():
    for x in range(1,101):
        for y in range(1,500):
            print(x)


if __name__ == "__main__":
    print(long_function())
