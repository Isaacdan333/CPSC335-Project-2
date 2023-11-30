def max_stocks(N, Stocks_and_values, Amount):
    # 2D array
    possible_stock = [[0] * (Amount + 1) for a in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(Amount + 1):
            # if the current stock value is greater than the available amount, skip it
            if Stocks_and_values[i - 1][1] > j:
                possible_stock[i][j] = possible_stock[i - 1][j]
                #print(dp)
            else:
                # Consider the maximum value of either including or excluding the current stock
                possible_stock[i][j] = max(possible_stock[i - 1][j], possible_stock[i - 1][j - Stocks_and_values[i - 1][1]] + Stocks_and_values[i - 1][0])
                #print(dp[i][j])

    return possible_stock[N][Amount]

N = 4
Stocks_and_values = [ [3, 2], [4, 3], [5, 3], [6, 7] ]
Amount = 10

result = max_stocks(N, Stocks_and_values, Amount)
#print(a)
print(result)
