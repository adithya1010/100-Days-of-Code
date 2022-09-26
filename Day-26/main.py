student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionary using for loop
#
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Loop through a data frame:
#
# for (key, value) in student_data_frame.items():
#     print(value)

# You can't work with the default for loop in pandas
# That's why pandas has a built-in function called iterrows() to iterate through DataFrames

# Loop through rows of a dataframe

for (index, row) in student_data_frame.iterrows():
    print(row.student)  # Each row is a series dataframe
    # Getting a particular student's score:
    if row.student == "Angela":
        print(row.score)
