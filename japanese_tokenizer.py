#
# Comp Ling PROJECT #2- Japanese Tokenization
#
# March 2019
# Author: Kelsey Broadfield kelseybroadfield@bennington.edu
#

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# how I run it on my computer bc I don't know how to use the terminal on my laptop
# input_file = 'in.txt'
# output_file = 'out.txt'

# creates list for japanese dictionary
word_checker = []

# opens japanese dictionary and writes it to a list
with open('japanese_wordlist.txt', 'r+', encoding="UTF-8") as my_list:
    for lines in my_list:
        words = my_list.readlines()
        lines.strip('\n')
        word_checker.append(words)

# creates lists, one is for the in text to be fixed and other is for fixed text
all_lines = []
spaced_lines = []

# this opens the japanese text without spaces and writes it to a list
with open(input_file, 'r+', encoding="UTF-8") as japanese_no_space:
    for x in japanese_no_space:
        lines = japanese_no_space.readline()
        all_lines.append(lines)


# creates list for function
my_new_lines = []


# defines function that reads japanese text and adds spaces between words
# PSA run program with parameters: all_lines and word_checker
def max_matcher(line, dictionary):
    for y in line:

        if y not in dictionary:
            current = y[:-1]
            my_new_lines.append(current)

        elif y in dictionary:
            spaced = y + ' '
            my_new_lines.append(spaced)

        else:
            max_matcher(line, dictionary)

        str_my_new_lines = str(my_new_lines)
        with open(output_file, 'w+', encoding="UTF-8") as spaced_text:
            spaced_text.write(str_my_new_lines)
            spaced_text.close()

        return my_new_lines


max_matcher(all_lines, word_checker)

# notes to self:
# first, read the whole line- and check within the dictionary for a match
# if there is no match, move back one character
# once there is a match, add a space


