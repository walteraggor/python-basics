# Defining a function and calling it.


def greet(name):
    return f"Hello, {name}!"


# This part runs only when the file is started directly (python greet.py).
# It is skipped when another file imports greet(), as greet_input.py does.
if __name__ == "__main__":
    print(greet("Walter"))
