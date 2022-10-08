# # Filenotfound Error - Happens when you try to read a file that doesn't exist
#
# # with open("a_file.txt") as file:
# #     file.read()
#
# # KeyError - happens when you try to access a key that doesn't exist in the dictionary
# # a_dictionary = {"key": "value"}
# # value = a_dictionary["non_existent_key"]
#
# # IndexError - happens when you try to get an element out of the range of the index
# # fruit_list = ["Apple", "Banana", "Pear"]
# # fruit = fruit_list[3]
#
# # TypeError
# # text = "abc"
# # print(text + 5)
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:  # Catching file not found error
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:  # Catching KeyError
#     print(f"The key {error_message} doesnt not exist")
# else:
#     content = file.read()
#     print(content)
# finally:  # Doesn't matter what happens it will execute
#     raise TypeError("This is an error that I made up")  # raise keyword is used to raise user-defined exception

# BMI Calculator
height = float(input("Height: "))
weight = int(input("Weight: "))
# If height entered is above 3 meters raise custom exception
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
