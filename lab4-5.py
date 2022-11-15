'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])

    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''

num_list = [1, 2, 3, 4, 5, 6]

def print_numbers(list):
    for i in range(0, len(list)):
        print(list[i])

def swapping_stars():
    line_str = ""
    for line in range(0, 6):
        for char in range(0,6):
            if char % 2:
                line_str += "*"
            else:
                line_str += "-"
    print(line_str)


#game loop
while True:
    which_function = input("Which funciton would you like to run? ")
    if which_function == '1':
        print_numbers(num_list)

    elif which_function =='2':
        swapping_stars()
    elif which_function == '3':
        print("Goodbye!")
        break
    else:
        print("That is not a function! (try 1,2, or 3)")