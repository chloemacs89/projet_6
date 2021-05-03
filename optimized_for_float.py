import csv
import sys


def make_list_from_csv(csv_file):
    with open(csv_file, newline='') as csv_f:
        share_file = csv.reader(csv_f, delimiter=",")
        share_list = []
        for i, row in enumerate(share_file):
            if not i:
                pass
            else:
                share_list.append((row[0], abs(int(float(row[1])*100)), float(row[2])/100 * float(row[1])))
    return share_list


shares_list = make_list_from_csv(sys.argv[1])

def total_value(combination):
    total_profit = 0
    total_val = 0
    for share, val, profit in combination:
        total_profit += profit
        total_val += val
    if total_val <= 500*100:
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
                try:
                    table[i][j] = max(table[i-1][j],
                                      table[i-1][j - int(val)] + profit)
                except IndexError:
                    import pdb; pdb.set_trace()

    best_result = []
    limit = max_limit

    for k in range(len(shares_list), 0, -1):
        is_added_to = table[k][limit] != table[k-1][limit]

        if is_added_to:
            share, val, profit = shares_list[k-1]
            best_result.append(shares_list[k-1])
            limit -= val

    return best_result


max_profit = knapsack_algorithm(shares_list, 50000)

share_to_buy = total_value(max_profit)

print("Buy the following shares : ",
      ", ".join([share for share, _, _ in max_profit]))

print("For a price of : ", share_to_buy[0]/100)
print("And a profit of : ", share_to_buy[1])
