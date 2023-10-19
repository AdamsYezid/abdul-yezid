# Ask user to input charge for the food
food_charge = float(input("enter the charge for the food: $"))

# Calculate the tip (18 percent)

tip_percentage = 0.18

tip_amount = food_charge * tip_percentage 

# Calculate sales tax

sales_tax_percentage = 0.07 

sales_tax_amount = food_charge * sales_tax_percentage 

#Calculate total cost of meal

total_cost = sales_tax_amount + tip_amount + food_charge 
print(tip_amount)
print(sales_tax_amount)
print(total_cost)



