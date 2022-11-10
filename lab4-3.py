'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''
#1
def draw_7():
    #prints 7 row
    for j in range(0,7):
        my_string = ''
        for i in range(0,6):
            my_string += ' *'
        print(my_string)



#2
def stars_and_stripes():
    for i in range(0,7):
        print()
        for j in range(0,7):
            if i ==1:
                print(' *', end='')
            if i ==2:
                print(' -', end='')
            if i ==3:
                print(' *', end='')
            if i == 4:
                print(' -', end='')
            if i == 5:
                print(' *', end='')
            if i == 6:
                print(' -', end='')
                
    

#3
def increasing_triangle():
    for i in range(0,8):
        print()
        for j in range(0,1):
            if i == 1:
                print("1")
            elif i == 2:
                print("1 2")
            elif i == 3:
                print("1 2 3")
            elif i == 4:
                print("1 2 3 4")
            elif i == 5:
                print("1 2 3 4 5") 
            elif i == 6:
                print("1 2 3 4 5 6 ")
            elif i == 7:
                print("1 2 3 4 5 6 7")   
                print()
            

    

#4 
def vertical_stars_and_stripes():
    for i in range(0,7):
        print()
        for j in range(0,6):
            if j % 2:
                print(' *', end='')
            else:
                print(' -', end='')


#5 
def made_up():
    for j in range(0,3): #loop 6 times
        my_string = ''
        for i in range(0,7):
            my_string += ' $'
        print(my_string)


while True:

    user_answer = input("What would you like to do? (draw_7, stars_and_stripes, increasing_triangle, vertical_stars_and_stripes, dollar_bill)")

    if user_answer == 'draw_7':
        draw_7()
    elif user_answer == 'stars_and_stripes':
        stars_and_stripes()
    elif user_answer == 'increasing_triangle':
        increasing_triangle()
    elif user_answer == 'vertical_stars_and_stripes':
        vertical_stars_and_stripes()
    elif user_answer == 'dollar_bill':
        made_up()
    else:
        print('')
        print("That is not an option ")


    