from functools import wraps

def exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        un_changed_function_return = func(*args, **kwargs)
        
        exclamation = un_changed_function_return + "!!!!!"
        
        return exclamation
    
    return wrapper
@exclamation
def say(txt):
    return txt


if __name__ == "__main__":
    print(say("Here we Go!"))
