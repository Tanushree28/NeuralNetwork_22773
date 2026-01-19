"""
Input the string “Python” as a list of characters from console, ['P', 'y'...]
delete at least 2 characters, reverse the resultant string and print it.

"""

# Input the string as a list of characters
char_list = list(input("Enter the string: ")) 

if ''.join(char_list) != "Python":
    print("Please enter the string 'Python' correctly.")

else:
    num_to_delete = int(input("How many characters to delete (at least 2): "))

    if num_to_delete < 2 or num_to_delete > len(char_list):
        print("Please enter a valid number.")
    else:
        deleted = 0
        while deleted < num_to_delete:
            char_to_delete = input(f"Enter character #{deleted+1} to delete (single letter): ")

            if len(char_to_delete) != 1:
                print("Enter exactly ONE character (example: t).")
                continue

            if char_to_delete in char_list:
                char_list.remove(char_to_delete)
                deleted += 1
            else:
                print(f"Character '{char_to_delete}' not found in the list.")

        char_list.reverse()
        print("Result:", ''.join(char_list))
        