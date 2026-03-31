def debugger(func):
    def before_and_after():
        print(f"before func {func.__name__}")
        func()
        print(f"affter func{func.__name__}")
    return before_and_after
