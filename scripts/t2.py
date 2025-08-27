import ast
import sys
start = ord('a')

# this scripts takes sorted_words.txt and basically initializes the letters struct
# dictionary.cc

with open("sorted_words.txt") as f:
    my_list = ast.literal_eval(f.read())

for i in range(0, 26):
    y = chr(start)
    x = f"letters.{y} = "
    print(x, end="")

    print("{ ", end="")

    for j in range(0, len(my_list)):
        word = my_list[j]
        if ord(my_list[j][0]) == start:  # print all skipped letters 
            if j == len(my_list) - 1:
                print(f'"{word}" ', end="")
            elif ord(my_list[j+1][0]) != start:
                print(f'"{word}" ', end="")
            else: 
                print(f'"{word}", ', end="")
    print("}")

    start += 1
    # print("letter.", chr(start), " = ")

