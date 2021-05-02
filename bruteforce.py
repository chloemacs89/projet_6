from itertools import combinations
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


def every_combinations(items_list):
    return (combin
            for i in range(1, len(items_list)+1)
            for combin in combinations(items_list, i)
    )


def total_value(combination):
    total_profit = 0
    total_val = 0
    for share, val, profit in combination:
        total_profit += profit
        total_val += val
    if total_val <= 500:
        return total_profit
    else:
        return 0


max_profit = max(every_combinations(shares_list),
                 key=total_value)

max_buy = sum([x[1] for x in max_profit])

share_to_buy = total_value(max_profit)

print("Buy the following shares : ",
      ", ".join([share for share, _, _ in max_profit]))
print("For a price of : ", max_buy)
print("And a profit of : ", (500-max_buy) + max_buy + share_to_buy)
