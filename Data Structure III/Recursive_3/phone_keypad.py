# ================================
#  PHONE KEYPAD COMBINATIONS
#  File: phone-keypad.py
# ================================

# PART 1 - KEYPAD MAPPING
keypad = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

# PART 2 - RECURSIVE FUNCTION
def combinations(digits, current):
    if len(digits) == 0:
        print(current)
        return

    # PART 3 - EXPLORE EACH LETTER
    first_digit = digits[0]
    remaining = digits[1:]

    for letter in keypad[first_digit]:
        combinations(remaining, current + letter)

# PART 4 - TAKE USER INPUT
number = input("Enter digits (e.g. 23): ")
print("All combinations:")
combinations(number, "")

# PART 5 - COUNT THE COMBINATIONS
count = 1
for digit in number:
    count = count * len(keypad[digit])
print("Total combinations:", count)
