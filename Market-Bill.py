while True:
  total = 0
  custom_Name = input("Enter your name -")
  while True:
    quantity = int(input("Enter Quantity of items"))
    items = int(input("Enter Number of items"))
    total = quantity*items
    repeat = input("Do you want to add more items(y/Y/n/N)")
    if repeat=='n' or repeat=='N':
      break
    print("_"*50)
    print("Name : ",custom_Name)
    print("Total Cost : ",total)
    print()
    print("*****Thank you for shopping with us****")
    print("_"*50)
    new_custom = input("Go to next customer(y/Y/n/N)")
    if new_custom=='n' or new_custom=='N':
      break