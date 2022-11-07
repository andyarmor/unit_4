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
user_answer = input("What would you like to do? (draw_7, stars_and_stripes, increasing_triangle, vertical_stars_and_stripes, made_up)")
#1
def draw_7():
    #prints 6 row
    for j in range(0,7):
        my_string = ''
        for i in range(0,6):
            my_string += ' *'
        print(my_string)



#2
def stars_and_stripes():
    star = ''
    for i in range(0,7):
        star += ' *'
        for j in range(0,7):
            dash = ''

    print(star)
    

#3
def increasing_triangle():
    
    pass

#4 
def vertical_stars_and_stripes():

    pass

#5 
def made_up():

    pass

if user_answer == 'draw_7':
    draw_7()
elif user_answer == 'stars_and_stripes':
    stars_and_stripes()
elif user_answer == 'increasing_triangle':
    increasing_triangle()
elif user_answer == 'vertical_stars_and_stripes':
    vertical_stars_and_stripes()
elif user_answer == 'made_up':
    made_up()


    