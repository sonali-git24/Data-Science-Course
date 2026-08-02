# DREAM RECURSION LAB
# Topics: What Is Recursion | Base Case | Build and Unwind
#         Count 1 to 10 | Factorial | Stack Overflow


# PART 1: What Is Recursion?
# Like Inception: a dream inside a dream inside a dream.
# A recursive function calls a smaller version of itself.
# Two rules: (1) call with a SMALLER problem each time.
#            (2) always have a BASE CASE to stop.

print("=== Dream Recursion Lab ===")
print("Two rules of recursion:")
print("  1. Call yourself with a SMALLER problem each time")
print("  2. Have a BASE CASE that stops the calls")
print()


# PART 2: Count 1 to 10 -- recursion going UP
# Base case: n > 10, stop.
# Recursive case: print n, then call with n + 1.

def count_up(n):
    if n > 10:          # base case: stop here
        return
    print(n, end=" ")
    count_up(n + 1)     # recursive call: n grows toward the base case

print("Counting 1 to 10 using recursion:")
count_up(1)
print()
print()


# PART 3: Countdown -- shows recursion BUILDING down then UNWINDING back up
# count_down(5) calls count_down(4), which calls count_down(3)...
# Each call WAITS. When base case hits, results bubble back up.

def countdown(n):
    if n == 0:          # base case
        print("Liftoff!")
        return
    print(n, end=" ")
    countdown(n - 1)    # recursive call: n shrinks toward 0

print("Countdown (builds down, unwinds up):")
countdown(5)
print()


# PART 4: Factorial -- recursion that multiplies on the way back up
# factorial(5) = 5 * factorial(4) = 5 * 4 * 3 * 2 * 1 = 120
# Base case: n == 0 or n == 1, return 1.
# Recursive case: n * factorial(n - 1).

def factorial(n):
    if n == 0 or n == 1:            # base case
        return 1
    return n * factorial(n - 1)     # recursive call: n shrinks

print("Factorial using recursion:")
print("factorial(5) =", factorial(5))
print("factorial(4) =", factorial(4))
print("factorial(1) =", factorial(1))
print("factorial(0) =", factorial(0))
print()


# PART 5: Stack overflow -- what happens with NO base case
# Python allows a maximum of 1000 recursive calls (default limit).
# Without a base case, calls never stop -- RecursionError: stack overflow!

import sys
print("Python recursion limit:", sys.getrecursionlimit(), "calls")

def no_base_case(n):
    print("Call", n, end=" ")
    no_base_case(n + 1)   # no base case -- this never stops!

sys.setrecursionlimit(30)   # tiny limit for safe demonstration
try:
    no_base_case(1)
except RecursionError:
    print()
    print("RecursionError! Stack overflow -- no base case!")

sys.setrecursionlimit(1000)
print("Rule: ALWAYS include a base case in every recursive function!")
