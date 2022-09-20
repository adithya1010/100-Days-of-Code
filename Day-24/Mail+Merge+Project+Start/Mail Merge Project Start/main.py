# Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
       #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()  # Reading the names in  invited names.txt file and saving it as a list using
    # readlines

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()  # saving the letter contents
    for name in names:
        stripped_name = name.strip()  # removing the \n that was added to each name at the end
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # Writing letters by replacing the
        # placeholder with the names
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter) # writing the completed letter in separate files
