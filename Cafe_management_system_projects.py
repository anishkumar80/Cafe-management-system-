print("**********WELCOME TO APNA RESTAURANT*************\n\n          `````````````````CAFE MENU``````````````````````")
print("----COLD-----\nButter Milk: 45.00\nSoda: 20.00\nMineral Water 1 ltr: 20.00\n\n",
      "----SOUTH INDIAN-----\nPoha: 45.00\nUpma: 45.00\nIdli dosa: 50.00\nSheera: 45.00\nMedu Wada (2pc): 70.00\n\n",
      "----SHAKES----\nChicko shake: 90.00\nBanana lassi: 100.00\nApple shake: 110.00\nPapaya shake: 80.00\nPapaya juice: 100.00",
      "Pineapple juice: 90.00\nWatermelon juice: 90.00\nMosambi juice: 150.00\nOrange juice: 120\nApple juice: 120\n\n",
      "-----LUNCH & DINNER----\nRoti (1pc): 5\nButter roti (ipc): 8\nDal fry(100ml):35\nRice (Half plate): 25\nRice fried (half plate): 45\nDal makhni (100ml):40\nAloo palak: 30\nPaneer matar(1plate):90")

menu = {
    'Butter Milk':45.00,
    'Soda':20.00,
    'Mineral Water':20.00,
    'Poha':45.00,
    'Upma':45.00,
    'Idli dosa':50.00,
    'Sheera':45.00,
    'Medu Wada':70.00,
    'Papaya juice':100.00,
    'Pineapple juice':90.00,
    'Watermelon juice':90.00,
    'Mosambi juice':150.00,
    'Orange juice':120.00,
    'Apple juice':120.00,
    'Chicko shake':90.00,
    'Banana lassi':100.00,
    'Apple shake':110.00,
    'Papaya shake':80.00,
    'Roti':5.00,
    'Butter roti':8.00,
    'Dal fry':35.00,
    'Rice':25.00,
    'Rice fried':45.00,
    'Dal makhni':40.00,
    'Aloo palak':30.00,
    'Paneer matar':90.00
    
    }

order_total = 0
order_total_1 = 0
item_1= input("\nEnter your order item = ")
if item_1 in menu:
    quantity = int(input("Enter Quantity of item = "))
    order_total_1 += menu[item_1]*quantity
else:
    print(f"Item {item_1} not Available")
for i in menu:
    other_order = input("\nDo you want to add another item (yes / no)")
    if (other_order == "yes" or other_order == "Yes" or other_order == "YES"):
        item = input("\nEnter your  order item = ")
        quantity = int(input("Enter Quantity of item = "))
        if item in menu:
            order_total += menu[item]*quantity
            print(f"Item {item} has been added to your order")
        else:
            print(f"Order item is not available")
    else:
        break
print("\nThank you for Visiting")
print(f"\n----PAY BILLS:-- \nThe total amount of items is {order_total_1 + order_total} Rupees\n\nPay amount on UPI NO. 8092278097")
    
