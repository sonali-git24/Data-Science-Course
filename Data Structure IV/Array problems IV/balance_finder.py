# array-problems-4-508-68-activity.py

# PART 1 - Slices and their sums
arr = [-4, 6, 2, 0, 0, 1, 1]
print("Full array:", arr)
print("Left of index 2 :", arr[:2])
print("Right of index 2:", arr[3:])
print("Left sum at index 2 :", sum(arr[:2]))
print("Right sum at index 2:", sum(arr[3:]))

# PART 2 - Balance at every index
print("\nBalance check:")
for i in range(len(arr)):
    L = sum(arr[:i])
    R = sum(arr[i + 1:])
    print("index", i, "-> left:", L, " right:", R)

# PART 3 - Equilibrium point
print("\nEquilibrium point:")
for i in range(len(arr)):
    if sum(arr[:i]) == sum(arr[i + 1:]):
        print("Index:", i, "  Element:", arr[i])

# PART 4 - Growing subarray window
nums = [3, 6, 2, 2, 56, 1, 0, 9]
target = 10
print("\nGrowing window (start = 1, target =", target, "):")
curr = 0
for j in range(1, len(nums)):
    curr += nums[j]
    print(" nums[1 to", j, "] =", nums[1:j + 1], " sum =", curr)
    if curr >= target:
        break

# PART 5 - Find subarray with target sum
print("\nSearching all windows:")
found = False
for i in range(len(nums)):
    if found:
        break
    curr = 0
    for j in range(i, len(nums)):
        curr += nums[j]
        if curr == target:
            print("Found! Indexes", i, "to", j, ":", nums[i:j + 1])
            found = True
            break
        if curr > target:
            break
if not found:
    print("No subarray found")
