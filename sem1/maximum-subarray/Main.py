import AppConstants

if __name__ == '__main__':
    print("\n\nMaximum Profit App Started")
    print("________________________________")

    def read_input_file():
        """
            Read File, Load Stock Prices
        """
        global file_content
        input_file = open(AppConstants.INPUT_FILE_NAME, "r")
        file_content += '\n\tA: Reading Stocks Data From File: \'' + AppConstants.INPUT_FILE_NAME + '\''
        for stock_row in input_file:
            stock_data = stock_row.rstrip().split("/")
            stock_list.append({
                'day': int(stock_data[0].lstrip().rstrip()),
                'price': int(stock_data[1].lstrip().rstrip())
            })
        input_file.close()
        file_content += '\n\tTotal Records: \'' + str(len(stock_list)) + '\''

    def maximum_profit_by_linear_method(stocks):
        global file_content
        maximum_profit = 0.0
        date_to_buy = stocks[0]['day']
        day_to_sell = stocks[1]['day']

        for i in range(len(stocks) - 1):
            for j in range(i+1, len(stocks)):
                if stocks[j]['price'] - stocks[i]['price'] > maximum_profit:
                    maximum_profit = stocks[j]['price'] - stocks[i]['price']
                    date_to_buy = stocks[i]['day']
                    day_to_sell = stocks[j]['day']

        file_content += '\tB. Maximum Profit (Iterative Solution): \'' + str(maximum_profit) + '\''
        file_content += '\n\tDay To Buy: \'' + str(date_to_buy) + '\''
        file_content += '\n\tDate To Sell: \'' + str(day_to_sell) + '\''
        file_content += '\n\tTime Complexity: "O(n^2)"'

    def maximum_profit_by_optimized_linear_method(stocks):
        global file_content
        maximum_profit = 0.0
        min_price = stocks[0]['price']
        date_to_buy = stocks[0]['day']
        day_to_sell = stocks[1]['day']

        for stock in stocks:
            if min_price > stock['price']:
                date_to_buy = stock['day']
            min_price = min(min_price, stock['price'])
            compare_profit = stock['price'] - min_price
            if compare_profit > maximum_profit:
                day_to_sell = stock['day']
            maximum_profit = max(maximum_profit, compare_profit)

        file_content += '\tC. Maximum Profit (Optimized Iterative Solution): \'' + str(maximum_profit) + '\''
        file_content += '\n\tDay To Buy: \'' + str(date_to_buy) + '\''
        file_content += '\n\tDate To Sell: \'' + str(day_to_sell) + '\''
        file_content += '\n\tTime Complexity: "O(n)"'


    def maximum_profit_by_divide_and_conquer_method(price_array):
        global file_content
        # Base case: If the array has zero or one elements in it, the maximum
        # profit is 0.
        if len(price_array) <= 1:
            return 0;

        # Cut the array into two roughly equal pieces.
        left = price_array[: len(price_array) / 2]
        right = price_array[len(price_array) / 2:]

        # Find the values for buying and selling purely in the left or purely in
        # the right.
        left_best = maximum_profit_by_divide_and_conquer_method(left)
        right_best = maximum_profit_by_divide_and_conquer_method(right)

        # Compute the best profit for buying in the left and selling in the right.
        cross_best = max(right) - min(left)
        maximum_profit = max(left_best, right_best, cross_best)

        if len(price_array) == len(stock_list):
            file_content += '\tD. Maximum Profit (Divide & Conquer): \'' + str(maximum_profit) + '\''
            file_content += '\n\tDay To Buy: \'' + str(left.index(min(left))) + '\''
            file_content += '\n\tDate To Sell: \'' + str(right.index(max(right))) + '\''
            file_content += '\n\tTime Complexity: "O(n log n)"'

        # Return the best of the three
        return maximum_profit


    def maximum_profit_by_optimized_divide_and_conquer_method(price_array):
        global file_content
        # If the array is empty, the maximum profit is zero.
        if len(price_array) == 0:
            return 0

        def recursion(array, lhs, rhs):
            # If the array has just one element, we return that the profit is zero
            # but the minimum and maximum values are just that array value.
            if lhs == rhs:
                return (0, array[lhs], array[rhs])

            # Recursively compute the values for the first and latter half of the
            # array.  To do this, we need to split the array in half.  The line
            # below accomplishes this in a way that, if ported to other languages,
            # cannot result in an integer overflow.
            mid = lhs + (rhs - lhs) / 2

            # Perform the recursion.
            (left_profit, left_min, left_max) = recursion(array, lhs, mid)
            (right_profit, right_min, right_max) = recursion(array, mid + 1, rhs)


            # Our result is the maximum possible profit, the minimum of the two
            # minimum we've found (since the minimum of these two values gives the
            # minimum of the overall array), and the maximum of the two maximum
            maxProfit = max(left_profit, right_profit, right_max - left_min)
            return (maxProfit, min(left_min, right_min), max(left_max, right_max))

        # Using our recursive helper function, compute the resulting value.
        profit, _, _ = recursion(price_array, 0, len(price_array) - 1)
        file_content += '\tE. Maximum Profit (Optimized Divide & Conquer): \'' + str(profit) + '\''
        file_content += '\n\tTime Complexity: "O(n)"'
        return profit


    stock_list = []
    file_content = ""

    file_content += '\n\n=============================================================================\n'
    read_input_file()
    file_content += '\n=============================================================================\n'

    maximum_profit_by_linear_method(stock_list)

    file_content += '\n=============================================================================\n'

    maximum_profit_by_optimized_linear_method(stock_list)

    file_content += '\n=============================================================================\n'
    stockPriceArray = [x['price'] for x in stock_list]
    maximum_profit_by_divide_and_conquer_method(stockPriceArray)

    file_content += '\n=============================================================================\n'
    maximum_profit_by_optimized_divide_and_conquer_method(stockPriceArray)

    print(file_content)

    """
       Write To outputPS5.txt
    """
    all_patient_output_file = open(AppConstants.OUTPUT_FILE_NAME, "w")
    all_patient_output_file.writelines(file_content)