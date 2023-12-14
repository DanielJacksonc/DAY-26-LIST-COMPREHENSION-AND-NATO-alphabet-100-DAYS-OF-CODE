# num = [1,2,3]
# new_num = []
# for i in num:
#     i+=1
#     new_num.append(i)
# print(new_num)

""" EXERCISE 1: This lesson was about list comprehension, I am going to write alist that would
get the square of all the numbers
the formula for writing list comprehension is : list = [new_item for item in list if condition]"""

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2/2 for number in numbers]
#
# print(squared_numbers)


""" EXERCISE 2: in this exercise, we will be using list comprehension to write a code that
 will filter out the even numbers from series   of numbers, and then convert it to a list of integers.
  then use the list comprehension to create a new list called result. this new list should contain only 
  even numbers from the list numbers"""

# list_of_strings = input().split(",")
#
# # use list comprehension to convert string to integers
# int_list = [int(i) for i in list_of_strings]
#
# result = [i for i in int_list if i%2 == 0]
#
# print(result)


"""EXERCISE 3: take a look at the file1 and file2, create a list called 
result that contains numbers that are common in both files"""

# with open("file1.txt", "r") as file1:
#     new_file1 = file1.readlines()
#
# with open("file2.txt") as file1:
#     new_file2 = file1.readlines()
#
# result = [int(num) for num in new_file1 if num in new_file2]
# print(result)
#
#
# with open ("our_common_file.txt", "w") as file:
#     file.write("new_file1_list")


""" ExEXERCISE 4: we will be taking a sentence and convert into a dictionary where the word in the 
sentence is the keys and the length of the word is the value including special symbols"""

# sentence = input()
# sentence_list = list(sentence.split())
#
# result = {word: len(word) for word in sentence_list}
#
# print(result)


"""EXERCISE 5: the purpose of this program is to take a temperature in celcius and convert it to Fahrenheit  """

# weather_c = eval(input())  # the val function coverts the string to a dictionary
#
# weather_f = {key: (value * 9/5) + 32 for key, value in weather_c.items()}
# print(weather_f)
