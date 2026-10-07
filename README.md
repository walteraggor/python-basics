# Simple Python Project

A handful of small scripts written while learning the basics of Python. Each file explores one idea and runs on its own.

| File | What it covers |
|---|---|
| `main.py` | Defining a function and calling it from an `if __name__ == '__main__':` block |
| `mpain.py` | The same greeting, but asking for the name with `input()` |
| `exercise.py` | Checking the type of a value with `type()`, and reassigning a variable |
| `hello.py` | A variable and an `if`/`else` branch |
| `newwaa.py` | Storing a string in a variable and printing it |

## Run a script

You need Python 3.6 or newer. There are no packages to install.

```bash
git clone https://github.com/walteraggor/simple-python-project.git
cd simple-python-project
python main.py
```

```
Hello, Walter!
```

Swap `main.py` for any other file in the table. For example, `python exercise.py` prints the type of several values:

```
42 -> int
3.14 -> float
42 -> str
True -> bool
None -> NoneType
99
```

The first and third lines look the same, but one is the number `42` and the other is the text `"42"`.
