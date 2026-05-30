# ============================================================
#   io_examples.py
#   Codeforces Input / Output — All Patterns with Examples
#   By: Tasnim Jabir
# ============================================================
#
#   HOW TO USE THIS FILE:
#   Run each section manually by commenting/uncommenting,
#   or just read it as a reference guide.
#
#   Each example shows:
#     - What the problem input looks like
#     - How to read it in Python
#     - How to print the output correctly
# ============================================================


# ────────────────────────────────────────────────────────────
# PATTERN 1: Read a single integer
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   5
#
# Task: Read n and print it doubled.

def pattern_1():
    n = int(input())      # input() reads a string, int() converts it
    print(n * 2)

# Expected output for input "5":  10


# ────────────────────────────────────────────────────────────
# PATTERN 2: Read two integers on one line
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   3 7
#
# Task: Print their sum and product.

def pattern_2():
    a, b = map(int, input().split())
    # input()       → "3 7"
    # .split()      → ["3", "7"]
    # map(int, ...) → converts each element to int
    # a, b = ...    → unpacks into two variables

    print(a + b)   # sum
    print(a * b)   # product

# Expected output:
#   10
#   21


# ────────────────────────────────────────────────────────────
# PATTERN 3: Read a list of integers (all on one line)
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   1 2 3 4 5
#
# Task: Print the sum and the maximum.

def pattern_3():
    nums = list(map(int, input().split()))
    # Result: nums = [1, 2, 3, 4, 5]

    print(sum(nums))   # → 15
    print(max(nums))   # → 5

# Expected output:
#   15
#   5


# ────────────────────────────────────────────────────────────
# PATTERN 4: Read n, then a list of n integers
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   5
#   10 20 30 40 50
#
# Task: Print average (integer division).

def pattern_4():
    n = int(input())
    nums = list(map(int, input().split()))

    print(sum(nums) // n)   # integer division for average

# Expected output:  30


# ────────────────────────────────────────────────────────────
# PATTERN 5: Read n lines, each with one integer
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   4
#   3
#   7
#   1
#   9
#
# Task: Print the numbers in reverse order.

def pattern_5():
    n = int(input())
    values = [int(input()) for _ in range(n)]

    for x in reversed(values):
        print(x)

# Expected output:
#   9
#   1
#   7
#   3


# ────────────────────────────────────────────────────────────
# PATTERN 6: Read a grid (matrix)
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   3 3
#   1 2 3
#   4 5 6
#   7 8 9
#
# Task: Print the sum of each row.

def pattern_6():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    for row in grid:
        print(sum(row))

# Expected output:
#   6
#   15
#   24


# ────────────────────────────────────────────────────────────
# PATTERN 7: Read a string
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   hello
#
# Task: Print it reversed and its length.

def pattern_7():
    s = input().strip()   # .strip() removes any accidental whitespace

    print(s[::-1])        # reverse the string
    print(len(s))         # length

# Expected output:
#   olleh
#   5


# ────────────────────────────────────────────────────────────
# PATTERN 8: Multiple test cases (most common on Codeforces!)
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   3
#   4
#   7
#   2
#
# Task: For each test case, print whether n is even or odd.

def pattern_8():
    t = int(input())          # number of test cases

    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            print("EVEN")
        else:
            print("ODD")

# Expected output:
#   EVEN
#   ODD
#   EVEN


# ────────────────────────────────────────────────────────────
# PATTERN 9: YES / NO output
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   3
#   4 2
#   5 3
#   9 3
#
# Task: Check if a is divisible by b. Print YES or NO.

def pattern_9():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        if a % b == 0:
            print("YES")
        else:
            print("NO")

# Expected output:
#   YES
#   NO
#   YES


# ────────────────────────────────────────────────────────────
# PATTERN 10: Printing a list (space-separated)
# ────────────────────────────────────────────────────────────
#
# Problem input:
#   5
#   3 1 4 1 5
#
# Task: Print the sorted list on one line.

def pattern_10():
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    print(*nums)         # * unpacks list → prints: 1 1 3 4 5
    # Same as: print(" ".join(map(str, nums)))

# Expected output:  1 1 3 4 5


# ────────────────────────────────────────────────────────────
# PATTERN 11: Fast input (for very large inputs)
# ────────────────────────────────────────────────────────────
#
# Use when input has 100,000+ lines. Faster than regular input().
#
# Just add these 2 lines at the top of your solution:

import sys
input = sys.stdin.readline   # override input() with faster version

# After this, use input() exactly the same way as before.
# Everything else stays the same!

def pattern_11():
    n = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))


# ────────────────────────────────────────────────────────────
# PATTERN 12: Read until end of input (no n given)
# ────────────────────────────────────────────────────────────
#
# Rare but it happens. The problem gives no count,
# just keeps giving input until it ends.
#
# Task: Sum all numbers given.

def pattern_12():
    import sys
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        total += int(line)
    print(total)


# ============================================================
# 🧩 COMPLETE TEMPLATE — Use this for most CF problems
# ============================================================

"""
import sys
input = sys.stdin.readline   # fast input

def solve():
    # Step 1: Read input
    n = int(input())
    nums = list(map(int, input().split()))

    # Step 2: Solve the problem
    answer = sum(nums)   # replace with your logic

    # Step 3: Print output
    print(answer)

# Read number of test cases and run
t = int(input())
for _ in range(t):
    solve()
"""

# If there's only ONE test case (no t), just call solve() directly:
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    # your logic here
    print(answer)

solve()
"""


# ============================================================
# 🚫 COMMON MISTAKES — What NOT to do
# ============================================================

# ❌ WRONG: This prints a prompt — Codeforces judge will get WA
# n = int(input("Enter n: "))

# ✅ CORRECT:
# n = int(input())

# ---

# ❌ WRONG: Adding extra text to output
# print("The answer is:", result)

# ✅ CORRECT:
# print(result)

# ---

# ❌ WRONG: Forgetting to convert string to int
# a, b = input().split()
# print(a + b)   # prints "37" not 10 if input is "3 7"

# ✅ CORRECT:
# a, b = map(int, input().split())
# print(a + b)   # prints 10

# ---

# ❌ WRONG: int() on a list
# nums = int(input().split())   # ERROR: can't convert list to int

# ✅ CORRECT:
# nums = list(map(int, input().split()))
