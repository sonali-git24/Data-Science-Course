# REVERSE LAB
# Topics: Digit Extraction | Reverse Number | Reverse String | Power of 4

print("=== Reverse Lab ===")
print()

# PART 1 — Digit Scanner
n = int(input("Enter a number: "))
temp = n
while temp > 0:
    print("  last digit:", temp % 10, "  remaining:", temp // 10)
    temp = temp // 10
print()

# PART 2 — Number Flipper
def flipNumber(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flipNumber(num // 10)
    return last * pow(10, len(str(rest))) + rest

n2 = int(input("Flip a number: "))
print(n2, "flipped ->", flipNumber(n2))
print()

# PART 3 — Name Flipper
def flipName(s):
    if len(s) == 1:
        return s
    return flipName(s[1:]) + s[0]

name = input("Enter your name: ")
print(name, "->", flipName(name))
print()

# PART 4 — Power of 4?
def isPower4(n):
    if n <= 0:
        return False      # stop — impossible
    if n == 1:
        return True       # stop — confirmed!
    if n % 4 == 0:
        return isPower4(n // 4)
    return False

print("16 ->", isPower4(16), "   12 ->", isPower4(12))
guess = int(input("Test your own number: "))
print(guess, "-> Power of 4?" , isPower4(guess))
