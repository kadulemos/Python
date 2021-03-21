sales_w1 = [7,3,42,19,15,35,9]
print(f'Sales week 1: {sales_w1}')
sales_w2 = [12,4,26,10,7,28]
print(f'Sales week 1: {sales_w2}')
sales = []

sales_w2.append(int(input('Sales in one day of week 2: ')))

sales.extend(sales_w1)
sales.extend(sales_w2)
#sales = sales_w1 + sales_w2

print(f'Total sales weeks: {sales}')

best_day_weeks = max(sales)
print(f'Best day profit: ${best_day_weeks}')

worst_day_weeks = min(sales)
print(f'Worst day profit: ${worst_day_weeks}')

print(f'Combined profit: ${best_day_weeks + worst_day_weeks}')