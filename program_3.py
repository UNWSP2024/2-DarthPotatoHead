#Program Written By: Ainsley Bellamy
#Date Written: 01/27/2025
#Program Title: displayTax_and_Total

def calculate_total_purchase():
    #empty array to fill
    item_prices = []
    #variable count to determine when the loop ends
    count = 0
    while count < 5:
        #user item price inputs
        price = float(input("Enter price of item: "))
        item_prices.append(price)
        count += 1
    #sum up prices
    subtotal = sum(item_prices)
    tax = float(0.07)
    #calculate amount of tax
    tax_amount = tax*subtotal
    #calculate tax + subtotal
    total = tax_amount+subtotal
    print(f'Subtotal: ${subtotal:.2f}\n'
          f'Tax Amount: ${tax_amount:.2f}\n'
          f'Total Plus Tax: ${total:.2f}')

calculate_total_purchase()