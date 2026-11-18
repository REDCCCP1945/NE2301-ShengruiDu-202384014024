# Python Course Practice — Exercise Set

**Beginner Python exercises completed as the course-practice part of NE2301**

| Item | Value |
| --- | --- |
| Course / class | NE2301 |
| Student | Shengrui Du (StevenDu) / 杜晟瑞 |
| Student ID | 202384014024 |
| Folder | `ShengruiDu_StevenDu_202384014024_CoursePractice` |
| Language | Python 3.12 (standard library only — no third-party packages required) |
| Companion work | `../ShengruiDu_StevenDu_202384014024_CourseDesign` — Qiang Heritage Digital Human knowledge-Q&A system |

All file, folder and identifier names in this package are English. The exercises are deliberately
small and self-contained: every script runs on its own, prints its own output, and can be read in
a couple of minutes.

---

## 1. Task checklist

| # | Task | File | Key concept |
| --- | --- | --- | --- |
| 0 | Install Python | `step_0_check_python_install.py` | Interpreter, `sys`, `platform` |
| 1 | Write Hello World in Python | `step_1_hello_world.py` | `print()` |
| 2 | Write Hello World in a Python function | `step_2_hello_world_function.py` | `def`, docstrings, `__main__` guard |
| 3 | Print Hello World **five times** using a loop | `step_3_hello_world_loop.py` | `for` + `range()` |
| 4 | Make a list of 5 numbers | `step_4_list_of_five_numbers.py` | Lists, `len()` |
| 5 | Print the list of 5 numbers | `step_5_print_list.py` | `enumerate()`, module import |
| 6 | Sort the list of 5 numbers and print it | `step_6_sort_list.py` | `sorted()` vs. `list.sort()` |

---

## 2. Environment

Python was already present on the machine and was verified rather than reinstalled:

```text
Version       : 3.12.0
Implementation: CPython
Executable    : C:\Users\th7\AppData\Local\Programs\Python\Python312\python.exe
Major.Minor   : 3.12
Status        : Python is installed and working.
```

If a fresh machine ever needs the interpreter, download it from
<https://www.python.org/downloads/>, tick **Add python.exe to PATH** during setup, then confirm
with `python --version` in a terminal. `step_0_check_python_install.py` performs the same check
from inside Python and prints the version, the implementation and the resolved interpreter path.

---

## 3. How to run

Open a terminal inside this folder and run any single step:

```powershell
cd ShengruiDu_StevenDu_202384014024_CoursePractice
python step_1_hello_world.py
```

Or run the whole set in one go, in order:

```powershell
Get-ChildItem -Filter 'step_*.py' | Sort-Object Name | ForEach-Object { "===== $($_.Name) ====="; python $_.Name; "" }
```

No virtual environment, no `pip install` and no configuration are needed — the scripts use only
the Python standard library.

---

## 4. What each exercise demonstrates

### Step 0 — Python installation check

Confirms that a working Python 3 interpreter is on the machine. `platform.python_version()`
returns the version string, `sys.executable` returns the path of the interpreter that is actually
running, and `sys.version_info` exposes the version as a comparable tuple.

### Step 1 — Hello World

The smallest complete Python program: a single `print()` call that writes text to the console.

```python
print("Hello, World!")
```

### Step 2 — Hello World inside a function

The same greeting, but wrapped in a function so it can be named, documented and reused. The
`if __name__ == "__main__":` guard keeps the call from firing when the module is imported by
another script.

```python
def say_hello() -> None:
    """Print the classic greeting."""
    print("Hello, World!")
```

### Step 3 — Hello World five times with a loop

Instead of repeating the same line by hand, `range(1, repeat_count + 1)` produces the sequence
`1, 2, 3, 4, 5` and the `for` body runs once per iteration — five greetings in total.

### Step 4 — A list of five numbers

`NUMBERS = [42, 17, 93, 8, 55]` creates a list literal. `make_list()` hands out a *copy* of it
with `list(NUMBERS)`, so that the later sorting step can never modify the original constant.
`len(numbers)` confirms the list holds exactly five items.

### Step 5 — Printing the list

The list is printed as a whole and then element by element using `enumerate(numbers, start=1)`,
which yields an index/value pair per element. The list is imported from step 4 with
`from step_4_list_of_five_numbers import make_list`, which shows how one module reuses another.

### Step 6 — Sorting the list

Two standard ways to sort, shown side by side:

- `sorted(numbers)` returns a **new** sorted list and leaves the original untouched — the
  preferred default because it is explicit and side-effect free.
- `numbers.sort()` sorts the list **in place** and returns `None` — convenient, but it mutates
  the object it is called on.

Both produce the same result here: `[8, 17, 42, 55, 93]`.

---

## 5. Verified output

```text
===== step_0_check_python_install.py =====
Python installation check
--------------------------------------------
Version       : 3.12.0
Implementation: CPython
Executable    : C:\Users\th7\AppData\Local\Programs\Python\Python312\python.exe
Major.Minor   : 3.12
--------------------------------------------
Status        : Python is installed and working.

===== step_1_hello_world.py =====
Hello, World!

===== step_2_hello_world_function.py =====
Hello, World!

===== step_3_hello_world_loop.py =====
1. Hello, World!
2. Hello, World!
3. Hello, World!
4. Hello, World!
5. Hello, World!

===== step_4_list_of_five_numbers.py =====
List of 5 numbers: [42, 17, 93, 8, 55]
Length of the list: 5

===== step_5_print_list.py =====
The list of 5 numbers is: [42, 17, 93, 8, 55]
Elements:
  1. 42
  2. 17
  3. 93
  4. 8
  5. 55

===== step_6_sort_list.py =====
Original list : [42, 17, 93, 8, 55]
Sorted (sorted): [8, 17, 42, 55, 93]
Sorted in place: [8, 17, 42, 55, 93]
```

---

## 6. File map

```text
ShengruiDu_StevenDu_202384014024_CoursePractice/
├── README.md                          # this document
├── step_0_check_python_install.py    # task 1 - verify the Python installation
├── step_1_hello_world.py             # task 2 - print Hello World
├── step_2_hello_world_function.py    # task 3 - print Hello World from a function
├── step_3_hello_world_loop.py        # task 4 - print Hello World five times with a loop
├── step_4_list_of_five_numbers.py     # task 5 - build a list of five numbers
├── step_5_print_list.py               # task 6 - print the list of five numbers
└── step_6_sort_list.py               # task 7 - sort the list and print it
```

**NE2301 ShengruiDu StevenDu 杜晟瑞 202384014024**
