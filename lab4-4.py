'''
############
Lab 4.04
############

Part 1
-----------
The goal of this lab is to practice using and accessing items from lists of lists.

You have a few errands to run and have created a few shopping lists to help you remember what to buy. 
You stored your notes in a nested list, shopping_cart. This program will allow the user to ask for a 
specific item by its index or update what items are in the cart. The user can request to view list to 
see the items in a specific shopping list.

Shopping Lists
    shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]
User Inputs
1 - Update

The program asks which shopping list the user wants to update, which position it should update, and the new value to update.

2 - View Item

The program asks which shopping list the item is on and which position it occupies, then prints the item's name.

3 - View List

The program asks which shopping list the user wants and prints all of the items associated with that shopping list.

Functions
update_list

Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new value for that item. Does not alter the length of the list.

print_item

Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.

print_list

Takes an int representing the index of the shopping list to print.

Feel free to add more functions as you see fit.

Example
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 1
    Which shopping list would you like to update? 1
    Which item would you like to change? 2
    New value for item #2? cheese
    toothpaste, cheese, milk
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 2
    Which shopping list do you want to choose? 2
    Which item on list #2 do you want to see? 3
    apples
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 3
    Which shopping list would you like to see? 3
    planner, pencils, q-tips

Part 2
------------
In this part of the lab you will go through your shopping list program and perform a few different calculations.

Create a function, all_in_one, that will put all the shopping lists into a single combined list using a for loop.

Create a function, count_q_tips, which will go through all items of the list and keep a count of how many times 
'q-tips' occurs.

In order to make the shopping lists more calcium rich, write a function, drink_more_milk, that adds 'milk' to each 
of the lists (unless it's already there).

You can't have milk without cookies. Write a function if_you_give_a_moose_a_cookie, that will go through every 
element of shopping_cart and update 'milk' to be 'milk and cookies'.

Extension
-------------
Write a function to reverse the order of the lists, and also reverse the order of the items in each list, in the shopping_cart nested list.

The new reversed list should look like the following when printed (newlines and spacing added for clarity):
'''

def update_list():
    which_list_answer = input("Which shopping list would you like to update? ")
    which_item = input("Which item would you like to change? ")
    updated_item = input(f"New value for item {which_item}? ")
    if which_list_answer == 1:
        which_list = shopping_lists[0]
        print(which_list)
    elif which_list_answer == 2:
        which_list = shopping_lists[1]
    elif which_list_answer == 3:
        which_list = shopping_lists[2]

    if which_item == 1:
        which_list.remove(shopping_lists[0][1])
    elif which_item == 2:
        pass
    elif which_item == 3:
        pass

def print_item():
    print("Hello")

    

def print_list():

    pass


user_input = input("Choose one: 1 = update item,  2 = view item  3 = view list: ")
shopping_lists = [['toothpaste', 'q-tips', 'milk'],['milk', 'candy', 'apples'],['planner', 'pencils', 'q-tips']]
while True:
    
    if user_input == 1:
        update_list()
    elif user_input == 2:
        print_item()
    elif user_input == 3:
        print_list()



#print(shopping_lists[2][0])



