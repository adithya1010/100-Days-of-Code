# # with open("./weather_data.csv", mode="r") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)
#
# import csv
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)  # Built-in csv file reader that automatically converts csv data to list type
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))  # Appending the temp column excluding the first one which is the name
# #             # of the column
# #     print(temperatures)
#
# # import pandas
# #
# # data = pandas.read_csv("weather_data.csv")  # Reading the CSV file using pandas
# #
# # # print(data["temp"])  # Printing the temp column from csv
# #
# # # Converting CSV data to dictionary
# #
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # Converting CSV column temp to list
#
# # Finding the average of the temp column
#
# # temp_list = data["temp"].to_list()
# # total = sum(temp_list)
# # avg = total / len(temp_list)
# # print(int(avg))
# #
# # # Using pandas built-in method to compute mean for series datatype
# # print(data["temp"].mean())
# # # Getting max value of temp using max method of pandas
# # # print(data["temp"].max())
# # # Pandas automatically converts column names to attributes
# # print(data.condition)
#
# # Working with rows:
#
# # Get data in row where day is Monday
#
# # print(data[data.day == "Monday"])
# #
# # # Get data where the temp is max
# #
# # print(data[data.temp == data.temp.max()])
#
# # Getting the condition data for monday
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# # # Converting monday's celsius data to fahrenheit
# # monday_temp = monday.temp
# # monday_fahrenheit = (monday_temp * 1.8) + 32
# # print(monday_fahrenheit)
#
# # Creating dataframe from scratch
# #
# # data_dict = {
# #     "students": ["Adithya", "Arihant", "Nithin"],
# #     "scores": [76, 56, 65]
# # }
# #
# # data = pandas.DataFrame(data_dict)  # Converting dictionary to dataframe using DataFrame() function
# # data.to_csv("new_data.csv")  # Converting the dataframe to csv file

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Printing the number of grey squirrels in the data using len()
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Converting the values to dictionary format
data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
# Converting the dictionary to csv format
df = pandas.DataFrame(data_dict)
df.to_csv("new_data_1.csv")

