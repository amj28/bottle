
import ast

with open("sorted_words.txt") as f:
    my_list = ast.literal_eval(f.read())

x = ord('a')
n = 0

for word in my_list:
    while ord(word[0]) > x:  # print all skipped letters
        print(chr(x), ":", n)
        x += 1
        n = 0
    n += 1

print(chr(x), ":", n)  # last group
