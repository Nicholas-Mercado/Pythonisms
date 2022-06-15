from functools import wraps
from time import time , sleep

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

def sleep_now(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper

@exclamation
@timer
@sleep_now
def say(txt):
    return txt


@timer
@sleep_now
def long_function():
    for x in range(1,101):
        for y in range(1,500):
            print(x)


if __name__ == "__main__":
    print(long_function())
