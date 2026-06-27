#used on that time where we dont know the number of arguments that will be passed in the function from user
#args collects the arguments in the form of tuple
#(*args) means multiple arguments are together


def  calculate_total_expenses(*expenses):
 print(f"expenses received:{expenses} ")
 return sum(expenses)
total_expenses=calculate_total_expenses(100,200,300,400)
print(f"total expenses:{total_expenses}")