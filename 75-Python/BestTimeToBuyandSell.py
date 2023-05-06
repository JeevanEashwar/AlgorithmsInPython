def best_time_to_buy_and_sell_stocks(prices):
    max_profit = 0
    buy_index = 0
    for sell_index in range(1, len(prices)):
        if prices[sell_index] < prices[buy_index]:
            buy_index = sell_index
        profit = prices[sell_index] - prices[buy_index]
        max_profit = max(max_profit, profit)
    return max_profit

print("##################################################")
print("###############      OUTPUT      #################")
print("##################################################")
print("best_time_to_buy_and_sell_stocks - [3,4,6,5,2,3,5,9,7,6,4]")
print("Maximum profit achievable - ", best_time_to_buy_and_sell_stocks([3,4,6,5,2,3,5,9,7,6,4]))
print("##################################################")
print("##################################################")