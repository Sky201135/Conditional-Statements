actual_cost = float(input("Enter the actual cost of the product: "))
sale_amount = float(input("Enter the sale amount: "))

if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
        print(f"The total profit = {amount}")
    else:
        print("No profit made on the sale.")