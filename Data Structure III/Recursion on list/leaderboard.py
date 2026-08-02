# ================================================
#  ACTIVITY - LEADERBOARD ANALYZER
#  File: leaderboard-analyzer.py
# ================================================

# PART 1 - THE HEAD-TAIL PATTERN
# a[0] is the HEAD — the first element we process
# a[1:] is the TAIL — the rest of the list passed to the next call

scores = [340, 120, 410, 85, 270, 190, 55]

print("=== PART 1: HEAD-TAIL PATTERN ===")
print("Full leaderboard    :", scores)
print("Head (scores[0])    :", scores[0])
print("Tail (scores[1:])   :", scores[1:])
print("Head of tail        :", scores[1:][0])
print("Tail of tail        :", scores[1:][1:])


# PART 2 - BASE CASE FOR LISTS
# When len(a) == 1 there is only one element left — nothing left to compare or split
# This is the base case that stops the recursion

def show_shrink(a, depth=0):
    indent = "  " * depth
    print(f"{indent}List: {a}  → length = {len(a)}")
    if len(a) == 1:
        print(f"{indent}Base case reached! Only one score left: {a[0]}")
        return
    show_shrink(a[1:], depth + 1)

print("\n=== PART 2: BASE CASE FOR LISTS ===")
show_shrink([410, 270, 190, 55])


# PART 3 - SORTED CHECK WITH RECURSION
# Check if a[0] <= a[1] AND check if the tail is also sorted
# Base case: a list of length 1 or 0 is always sorted

def is_sorted(a):

    # Base case — a single element is always in order
    if len(a) <= 1:
        return True

    # If the first score is greater than the next, it is not sorted
    # Otherwise check the rest of the list
    return a[0] <= a[1] and is_sorted(a[1:])

print("\n=== PART 3: SORTED CHECK ===")
print("Scores              :", scores)
print("Is sorted?          :", is_sorted(scores))

ranked = [55, 85, 120, 190, 270, 340, 410]
print("Ranked scores       :", ranked)
print("Is ranked sorted?   :", is_sorted(ranked))


# PART 4 - SUM OF A LIST WITH RECURSION
# Add the head to the sum of the tail
# The total builds back up as each call returns

def total_score(a):

    # Base case — a single element, just return it
    if len(a) == 1:
        return a[0]

    # Return head + sum of the rest
    return a[0] + total_score(a[1:])

print("\n=== PART 4: SUM WITH RECURSION ===")
print("Scores              :", scores)
print("Total team score    :", total_score(scores))


# PART 5 - LARGEST ELEMENT WITH RECURSION
# Compare the head against the largest value in the tail
# max() picks the bigger of the two

def top_score(a):

    # Base case — a single element is automatically the largest
    if len(a) == 1:
        return a[0]

    # Return the larger of head vs max of the rest
    return max(a[0], top_score(a[1:]))

print("\n=== PART 5: LARGEST ELEMENT ===")
print("Scores              :", scores)
champion = top_score(scores)
print("Champion's score    :", champion)
print("Champion is Player  :", scores.index(champion) + 1)
