# TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    f = open("./Input/Names/invited_names.txt","r")
    final_lines = f.readlines()
    for lines in final_lines:
        #if new_lines.strip():
           #lines = new_lines.strip()
        new_content = contents.replace("[name]",f"{lines.strip()}")
        with open(f"./Output/ReadyToSend/letter_for_{lines.strip()}.txt", mode="w") as new_file:
            new_file.write(new_content)
        print(new_content)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
