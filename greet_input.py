# The same greeting, but for a name typed by the user.
# greet() is not written out a second time: it is imported from greet.py.

from greet import greet

if __name__ == "__main__":
    user_name = input("Enter your name: ").strip()  # strip() removes spaces around the name
    if user_name == "":
        user_name = "stranger"
    print(greet(user_name))
