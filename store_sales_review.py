#products = ['Sankofa Foods', 'Jamestown Coffee', 'Bioko Chocolate', 'Blue Skies Ice Cream', 'Fair Afric Chocolate', 'Kawa Moka Coffee', 'Aphro Spirit', 'Mensado Bissap', 'Voltic']

#prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]


#Total price average
#total_price = 30 + 25 + 40 + 20 + 20 + 35 + 45 + 50 + 30

#print(total_price)

#no_of_products = 9

#average_price = total_price / no_of_products 

#print(average_price)

import statistics
total_p = {
    'Sankofa Foods': 30,
    'Jamestown Coffee': 25,
    'Bioko Chocolate': 40,
    'Blue Skies Ice Cream': 20,
    'Fair Afric Chocolate': 20,
    'Kawa Moka Coffee': 35,
    'Aphro Spirit': 45,
    'Mensado Bissap' : 50,
    'Voltic': 30,
}

no_of_items = 9
print(sum(total_p.values()))

total_price_average = statistics.mean(total_p.values())

print('The total price average is: ', total_price_average)




