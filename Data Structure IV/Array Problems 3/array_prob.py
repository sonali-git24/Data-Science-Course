# ARRAY PROBLEMS 3
# Topics: Binary arrays | Streak counter with reset | Best-streak tracker | Same-direction two pointers | Write-pointer pattern

# PART 1 -- Streak Counter with Reset
binary = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
streak = 0
for num in binary:
    if num == 0:
        streak = 0
    else:
        streak += 1
    print(num, "->", streak)
print()

# PART 2 -- Best-Streak Tracker
streak = 0
best = 0
for num in binary:
    if num == 0:
        streak = 0
    else:
        streak += 1
        if streak > best:
            best = streak
print("Binary array:", binary)
print("Max consecutive 1s:", best)
print()

# PART 3 -- Same-Direction Two Pointers
nums = [1, 0, 3, 6, 0, 0, 0, 2, 355, 0, 72]
print("Before:", nums)
zero = 0
for nonzero in range(len(nums)):
    if nums[nonzero] != 0:
        nums[nonzero], nums[zero] = nums[zero], nums[nonzero]
        zero += 1
print("After: ", nums)
print()

# PART 4 -- Write-Pointer Result
print("Write pointer stopped at:", zero)
print("Non-zeros at front:      ", zero)
print("Zeros at end:            ", len(nums) - zero)
