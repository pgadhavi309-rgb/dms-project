def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Function '{func.__name__}' called")
        return func(*args, **kwargs)
    return wrapper
    