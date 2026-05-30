# 📥📤 Input & Output in Codeforces — Complete Guide

> *The #1 reason beginners get Wrong Answer isn't logic — it's input/output. Let's fix that.*

---

## 🤔 Why Does I/O Matter So Much?

On Codeforces, your program **reads data from the keyboard** (stdin) and **prints answers to the screen** (stdout).

The judge compares your output **character by character** with the expected answer.
One wrong space, one missing newline — and it's **Wrong Answer (WA)**.

So before worrying about algorithms, get I/O right. ✅

---

## 📌 The Golden Rules

| Rule | Why |
|---|---|
| Read **exactly** what the problem says | Not more, not less |
| Print **exactly** what is asked | Spacing, newlines, format |
| Don't print extra messages | No `"Enter a number:"` prompts — ever |
| Don't worry about closing input | Python handles it automatically |

---

## 📖 Understanding the Problem Format

Every Codeforces problem has an **Input** and **Output** section.

**Example problem:**
```
Input:
5
1 2 3 4 5

Output:
15
```

This means:
- First line → one number `n = 5`
- Second line → `n` numbers separated by spaces
- Output → their sum `15`

---

## 1️⃣ Reading a Single Number

**Problem says:** *"The first line contains an integer n."*

```python
n = int(input())
```

`input()` reads a line as a **string**.
`int()` converts it to a number.

---

## 2️⃣ Reading Two or More Numbers on One Line

**Problem says:** *"The first line contains two integers a and b."*

```
Input: 3 7
```

```python
a, b = map(int, input().split())
```

**How it works:**
- `input()` → `"3 7"`
- `.split()` → `["3", "7"]`
- `map(int, ...)` → converts each to int
- `a, b = ...` → unpacks into variables

---

## 3️⃣ Reading a List of Numbers

**Problem says:** *"The second line contains n integers."*

```
Input: 1 2 3 4 5
```

```python
nums = list(map(int, input().split()))
```

Result: `nums = [1, 2, 3, 4, 5]`

---

## 4️⃣ Reading Multiple Lines (n rows)

**Problem says:** *"The next n lines each contain one integer."*

```
Input:
3
10
20
30
```

```python
n = int(input())
for i in range(n):
    x = int(input())
    # do something with x
```

Or collect them all into a list:

```python
n = int(input())
values = [int(input()) for _ in range(n)]
```

---

## 5️⃣ Reading a Grid / Matrix

**Problem says:** *"The next n lines each contain m integers."*

```
Input:
3 3
1 2 3
4 5 6
7 8 9
```

```python
n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
```

Or one-liner:
```python
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
```

---

## 6️⃣ Reading a String

**Problem says:** *"The first line contains a string s."*

```python
s = input()          # reads as string, no conversion needed
s = input().strip()  # safe version — removes accidental spaces/newlines
```

---

## 7️⃣ Reading Until End of Input (no n given)

Sometimes the problem gives no `n` — just keep reading until there's nothing left.

```python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # process line
```

---

## 8️⃣ Multiple Test Cases

**Problem says:** *"The first line contains t — the number of test cases."*

```
Input:
3
5
10
7
```

```python
t = int(input())
for _ in range(t):
    n = int(input())
    # solve for n
    print(answer)
```

This is **extremely common** on Codeforces. Almost every problem has `t` test cases.

---

## 📤 Output Rules

### Print a single answer
```python
print(42)
```

### Print multiple values on one line (space-separated)
```python
a, b = 3, 7
print(a, b)          # → "3 7"  (print adds spaces automatically)
```

### Print a list space-separated
```python
nums = [1, 2, 3, 4, 5]
print(*nums)          # → "1 2 3 4 5"
```

The `*` unpacks the list. This is a very common Codeforces trick.

### Print each item on its own line
```python
for x in nums:
    print(x)
```

### Print "YES" or "NO" (very common!)
```python
if condition:
    print("YES")
else:
    print("NO")
```

> ⚠️ Check if the problem wants `YES/NO`, `Yes/No`, or `yes/no`. They're different!

---

## ⚡ Fast Input (for large inputs)

For problems with **very large input** (100,000+ numbers), `input()` can be slow.
Use this faster method:

```python
import sys
input = sys.stdin.readline
```

Just add this at the **top of your code**. Everything else stays the same.
This is a habit most competitive programmers develop early.

---

## 🧩 Putting It All Together — Template

This is a starting template you can use for almost any Codeforces problem:

```python
import sys
input = sys.stdin.readline  # fast input

def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    # --- your logic here ---
    answer = sum(nums)
    # -----------------------

    print(answer)

t = int(input())
for _ in range(t):
    solve()
```

If there's no `t` (just one test case), remove the loop and call `solve()` once.

---

## 🚫 Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| `input("Enter n: ")` | Prints a prompt — judge hates this | Use `input()` with no arguments |
| `print("Answer:", x)` | Extra text in output | Use `print(x)` only |
| `int(input().split())` | `split()` returns a list, can't convert directly | Use `map(int, input().split())` |
| Forgetting to convert | `"3" + "7"` = `"37"` not `10` | Always `int()` numbers |
| Extra blank lines | Judge may mark WA | Be careful with `print()` |

---

## 🔍 Quick Reference Cheat Sheet

```python
# Single integer
n = int(input())

# Single float
x = float(input())

# Two integers on one line
a, b = map(int, input().split())

# List of integers
nums = list(map(int, input().split()))

# String
s = input().strip()

# n lines of input
data = [int(input()) for _ in range(n)]

# Grid (n rows, m cols)
grid = [list(map(int, input().split())) for _ in range(n)]

# t test cases
t = int(input())
for _ in range(t):
    # solve here

# Print list space-separated
print(*nums)

# Fast input (for big inputs)
import sys
input = sys.stdin.readline
```

---

## 🎯 Key Takeaways

1. **`input()`** reads a line as a string — always convert numbers with `int()` or `float()`
2. **`.split()`** breaks a line by spaces — use with `map(int, ...)` for number lists
3. **`print(*list)`** is the cleanest way to print a list space-separated
4. **`sys.stdin.readline`** speeds things up for large inputs
5. **Never print extra text** — the judge only checks exact output

---

*See `io_examples.py` for all of these patterns as runnable code with comments.*
