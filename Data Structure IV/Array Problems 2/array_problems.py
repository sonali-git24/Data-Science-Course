# ARRAY PROBLEMS 2
# Topics: Stocks buy-sell | Left tallest bars | Right tallest bars | Rainwater trapped

# PART 1 -- Stocks Buy-Sell
prices = [100, 180, 260, 310, 40, 535, 695]
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
print("Stock prices:", prices)
print("Maximum profit:", profit)
print()

# PART 2 -- Left Tallest Bars
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(heights)
left_tallest = [0] * n
left_tallest[0] = heights[0]
for i in range(1, n):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])
print("Heights:      ", heights)
print("Left tallest: ", left_tallest)
print()

# PART 3 -- Right Tallest Bars
right_tallest = [0] * n
right_tallest[n - 1] = heights[n - 1]
for i in range(n - 2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], heights[i])
print("Right tallest:", right_tallest)
print()

# PART 4 -- Rainwater Trapped
water = 0
for i in range(n):
    water += min(left_tallest[i], right_tallest[i]) - heights[i]
print("Total water trapped:", water)
