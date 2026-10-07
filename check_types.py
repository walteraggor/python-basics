# Checking the type of a value with type(), and what happens when a variable is reassigned.

values = [42, 3.14, "42", True, None]

for v in values:
    print(v, "->", type(v).__name__)

# y is given the value that x has at this moment.
# Changing x afterwards does not change y.
x = 10
y = x
x = 99
print("x =", x)
print("y =", y)
