def calculate_total_cost(price,qty,discount,tax):
    total=sum([price*qty for price,qty in zip(price,qty)])
    total*=(1-discount/100)
    total*=(1+tax/100)
    return total
price=[10,20]
qty=[3,2]
discount=10
tax=5
total=calculate_total_cost(price,qty,discount,tax)
print(f"The total cost for this purchase would be {total:.1f}.")
