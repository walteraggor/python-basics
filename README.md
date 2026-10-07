# Simple Python Project

A handful of small scripts written while learning the basics of Python. Each file explores one idea and runs on its own.

| File | What it covers |
|---|---|
| `greet.py` | Defining a function and calling it from an `if __name__ == '__main__':` block |
| `greet_input.py` | The same greeting, but asking for the name with `input()` |
| `check_types.py` | Checking the type of a value with `type()`, and reassigning a variable |
| `if_else.py` | A variable and an `if`/`else` branch |
| `print_variable.py` | Storing a string in a variable and printing it |

## Run a script

You need Python 3.6 or newer. There are no packages to install.

```bash
git clone https://github.com/walteraggor/simple-python-project.git
cd simple-python-project
python greet.py
```

```
Hello, Walter!
```

Swap `greet.py` for any other file in the table. For example, `python check_types.py` prints the type of several values:

```
42 -> int
3.14 -> float
42 -> str
True -> bool
None -> NoneType
99
```

The first and third lines look the same, but one is the number `42` and the other is the text `"42"`.
