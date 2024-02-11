def maxProfit(prices) -> int:
    # Initialize variables to track the minimum price and maximum profit
    mini = prices[0]
    profit = 0

    # Iterate through the prices list starting from the second element
    for i in range(1, len(prices)):
        # Calculate the profit that can be achieved if we sell at the current price
        cost = prices[i] - mini
        # Update the maximum profit seen so far
        profit = max(cost, profit)
        # Update the minimum price seen so far
        mini = min(mini, prices[i])

    # Return the maximum profit
    return profit


# Example usage of the maxProfit function
prices = [7, 1, 5, 3, 6, 4]
max_profit = maxProfit(prices)
print("Maximum profit:", max_profit)
