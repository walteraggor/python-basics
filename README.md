# Python Basics

A handful of small scripts written while learning the basics of Python. Each file explores one idea, says which one in a comment at the top, and can be run on its own.

| File | What it covers |
|---|---|
| `print_variable.py` | Storing a string in a variable and printing it |
| `if_else.py` | A variable and an `if`/`else` branch |
| `check_types.py` | Checking the type of a value with `type()`, and reassigning a variable |
| `greet.py` | Defining a function and calling it from an `if __name__ == "__main__":` block |
| `greet_input.py` | Asking for a name with `input()`, and reusing a function from another file with `import` |

The table goes from the simplest script to the one that uses the most ideas.

## Run a script

You need Python 3.6 or newer. There are no packages to install.

```bash
git clone https://github.com/walteraggor/python-basics.git
cd python-basics
python greet.py
```

```
Hello, Walter!
```

Swap `greet.py` for any other file in the table.

## What to look for

**`check_types.py`** prints the type of several values, then shows what reassigning a variable does:

```
42 -> int
3.14 -> float
42 -> str
True -> bool
None -> NoneType
x = 99
y = 10
```

The first and third lines look the same, but one is the number `42` and the other is the text `"42"`.

The last two lines come from setting `y = x` while `x` was 10 and then changing `x` to 99. `y` is still 10, because it was given the value `x` had at that moment and is not tied to `x` afterwards.

**`greet_input.py`** asks for a name and greets it:

```
Enter your name: Ada
Hello, Ada!
```

It does not have a `greet()` function of its own. It imports the one in `greet.py`, which is why `greet.py` keeps its own greeting inside `if __name__ == "__main__":`. That block runs when you start `greet.py` directly and is skipped when the file is imported, so `Hello, Walter!` is not printed here.
