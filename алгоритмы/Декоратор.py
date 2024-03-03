

from functools import wraps

def debug(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print("Name function", f.__name__)
        print("Function args", args)
        print("Function kwargs", kwargs)
        result = f(*args, **kwargs)
        print("Result", result)
        return result
    return inner
