
values = [42, 3.14, "42", True, None]

for v in values:
    print(v, "->", type(v).__name__)

x = 10
y = x
x = 99
print(x)

