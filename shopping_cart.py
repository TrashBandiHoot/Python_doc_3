import os

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

shopping_list = []

    
def Add():
    os.system('cls')
    new_item = input("What would you like to add?: ")
    shopping_list.append(new_item)
    print(f"{new_item} has been added to the cart")
    
    repeat = input("Would you like to add another item? 'Y' or 'N': ")
    
    if repeat == 'y':
        Add()
    
    
def Delete():
    os.system('cls')
    print(f"Shopping list: {shopping_list}")
    del_item = input("What would you like to delete?: ")
    
    try:
        shopping_list.remove(del_item)
        repeat = input("Would you like to delete another item? 'Y' or 'N': ")
    except:
        repeat = input("That item doesn't exist, would you like to delete a different item? 'Y' or 'N': ")
    
    if repeat == 'y':
        Delete()
    

run = True

while run:
    flag = input("Would you like to edit the shopping cart? 'Y' or 'N': ").lower()
    
    if flag == 'n':
        print(f"Shopping list: {shopping_list}")
        break

    user_choice = input("What would you like to do? Show/Add/Delete: ").lower()

    if user_choice == 'show':
        print(f"Shopping list: {shopping_list}")
    elif user_choice == 'add':
        Add()
    elif user_choice == 'delete':
        Delete()