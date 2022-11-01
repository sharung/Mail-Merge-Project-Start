# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name:
    name = name.readlines()

with open("Input/Letters/starting_letter.txt") as latter:
    latter_content = latter.read()
    for nama in name:
        strip_name = nama.strip()
        new_latter = latter_content.replace(PLACEHOLDER, strip_name)
        with open(f"Output/ReadyToSend/latter_for_{strip_name}", mode="w") as complit_latter:
            complit_latter.write(new_latter)
