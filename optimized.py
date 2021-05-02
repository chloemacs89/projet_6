import csv


def make_list_from_csv(csv_file):
    with open(csv_file, newline='') as csv_f:
        share_file = csv.reader(csv_f, delimiter=",")
        share_list = []
        for i, row in enumerate(share_file):
            if not i:
                pass
            else:
                share_list.append((row[0], int(row[1]), float(row[2]) * int(row[1])))
    return share_list


shares_list = make_list_from_csv("./actions.csv")


def total_value(combination):
    total_profit = 0
    total_val = 0
    for share, val, profit in combination:
        total_profit += profit
        total_val += val
    if total_val <= 500:
        return (total_val, total_profit)
    else:
        return (0, 0)


def knapsack_algorithm(shares_list, max_limit):
    table = [[0 for x in range(max_limit + 1)]
             for y in range(len(shares_list) + 1)]

    for i in range(1, len(shares_list) + 1):
        share, val, profit = shares_list[i - 1]
        for j in range(1, max_limit + 1):
            if val > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j],
                                  table[i-1][j - val] + profit)

    best_result = []
    limit = max_limit

    for k in range(len(shares_list), 0, -1):
        is_added_to = table[k][limit] != table[k-1][limit]

        if is_added_to:
            share, val, profit = shares_list[k-1]
            best_result.append(shares_list[k-1])
            limit -= val

    return best_result


max_profit = knapsack_algorithm(shares_list, 500)

share_to_buy = total_value(max_profit)

print("Buy the following shares : ",
      ", ".join([share for share, _, _ in max_profit]))

print("For a price of : ", share_to_buy[0])
print("And a profit of : ",
      (500-share_to_buy[0])
      + share_to_buy[0]
      + share_to_buy[1])
