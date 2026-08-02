# RECURSION PATTERNS
# Topics: Linear | Tail | Head | Increasing-Decreasing | Tree Recursion


# PART 1: Linear Recursion — one call per level, one path down
def linear(n):
    if n == 0:
        return
    print(n, end=" ")
    linear(n - 1)        # exactly ONE recursive call

print("Linear recursion (one call per level):")
linear(5)
print()


# PART 2: Tail Recursion — call is LAST, work goes DOWN
def tail(n):
    if n == 0:
        return
    print(n, end=" ")    # work first
    tail(n - 1)          # call last

print("Tail recursion (prints going down):")
tail(5)
print()


# PART 3: Head Recursion — call is FIRST, work comes UP on unwind
def head(n):
    if n == 0:
        return
    head(n - 1)          # call first
    print(n, end=" ")    # work on unwind

print("Head recursion (prints coming up):")
head(5)
print()


# PART 4: Increasing-Decreasing — work on BOTH sides of the call
def inc_dec(n):
    if n == 0:
        return
    print(n, end=" ")    # going down
    inc_dec(n - 1)
    print(n, end=" ")    # coming back up

print("Increasing-Decreasing (down then up):")
inc_dec(4)
print()


# PART 5: Tree Recursion — TWO calls per level, branches double
def tree(n):
    if n == 0:
        return
    print(n, end=" ")
    tree(n - 1)          # first branch
    tree(n - 1)          # second branch

print("Tree recursion (two calls -- branches double):")
tree(3)
print()
print("Level calls: 1 -> 2 -> 4 -> 8  (doubles every level!)")
