'''
Lab 4.01

Remove the Vowels
Create a function, de_vowel, which will take a string as input and return a copy of that string with all the vowels removed. Otherwise, the string should be the same. 'Y' does not count as a vowel for the purposes of this function.

Create the function contract for de_vowel.

Write de_vowel using a for loop

Provide a few examples that confirm de_vowel works as expected:

What if the string is all vowels?

What if there are no vowels?

What if there is a mix of vowels and non-vowels and spaces?

What if some vowels are capitalized, e.g., the first letter in a sentence?

Example
Example of the file:

    # contract goes here
    def de_vowel(a_string):
        # your code goes here

    no_vowels = de_vowel("This sentence has no vowels")
    print(no_vowels)
    # examples go here
Example output:

    >>> python3 de_vowel_lab.py
    Ths sntnc hs n vwls
Bonus
Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function count_vowels.

count_vowels takes in a string and returns an int representing the number of vowels in the string.

Can you think of an alternate way to do complete this task without any loop or counter, by making use of your new de_vowel() function instead?
'''
def de_vowel(a_sentence):
     VOWELS = 'aeiou'
     no_vowel_sentence = ""

     for letter in a_sentence:
         if letter not in a_sentence:
             no_vowel_sentence +=letter
     return no_vowel_sentence

def count_vowels(a_sentence):
    #function to return a count of the number of vowels in the sentence
    counter = 0
    for letter in a_sentence:
        if letter in VOWELS:
            counter +=1
    return counter
# tell user how many vowels there are

# print the sentence without vowels
VOWELS = 'aeiou'
the_sentence = input("What sentence do you want to de-vowel? ")

print(f"There are {count_vowels(the_sentence)} vowels in your sentence")
print()
print(f"Here's your sentence without vowels:")
print(de_vowel(the_sentence))


