def stock_maximization(N, Stocks_and_values, Amount):
    max_stocks = 0
    

    # make all possible combinations
    for i in range(2**N):
        current_stock = 0
        current_value = 0
        combinations = []

        for j in range(N):
            if (i >> j) & 1:
                current_stock += Stocks_and_values[j][0]
                current_value += Stocks_and_values[j][1]
                combinations.append(j)

        #check to see if combination valid and maximizes # of stocks
        if current_value <= Amount and current_stock > max_stocks:
            max_stocks = current_stock

    return max_stocks

N = 0
Stocks_and_values = [[1, 2], [4, 3], [5, 6], [6, 7]]
Amount = 12

for i in Stocks_and_values:
    N += 1

if N > 0 and N < 1000:
    result = stock_maximization(N, Stocks_and_values, Amount)
    print("Maximum number of stocks:", result)
else:
    print("Invalid constraints")
