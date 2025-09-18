def decorator_func(func):
    def wallpaper():
        print("Starting function")
        result = func()
        print("Finished function")
        return result
    return wallpaper

def greet():
    return "Hello Pragnesh"

decorated_greet = decorator_func(greet)
print(decorated_greet())