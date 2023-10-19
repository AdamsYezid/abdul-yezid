
total = int(input("Enter the amount of the item: "))
state = input("Enter the sate name in USA: ")
if state == "Florida":
    if total <= 50:
        print("Shipping cost is $50")
elif total > 50 and total <= 100:
    print("Shipping cost in Florida is $30")
else:
        print("Shipping cost in Florida is $10")

if state == "Chicago":
    if total <= 50:
        print("Shpping to Chicago in USA is $100")
    elif total > 50 and total <=100:
        print("Shipping to Chicago is $60")
    else:
        print("Shipping to Chicago is $15")

else:
    print("Invalid state")
