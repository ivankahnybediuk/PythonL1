"""
Write a program, which has two print statements to print the following text (capital letters “O” and “H”, made from “#” symbols):

#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #
Pay attention that usage of spaces is forbidden, as well as creating the whole result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.


"""

print('#########'+f'\n#\t#'*3+f'\n#########')
print(f'\n#\t#'*2+f'\n#########'+f'\n#\t#'*2)