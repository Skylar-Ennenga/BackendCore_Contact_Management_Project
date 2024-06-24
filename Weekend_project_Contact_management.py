
# Project Requirements

# Your task is to develop a Contact Management System with the following features:

#     User interface (UI):

#         Create a user-friendly command-line interface (CLI) for the Contact Management System.

#         Display a welcoming message and provide a menu with the following options:

#         Menu:
#         Add a new contact
#         Edit an existing contact
#         Delete a contact
#         Search for a contact
#         Display all contacts
#         Export contacts to a text file
#         Import contacts from a text file
#         Quit 


#     Contact Data Storage:

#         Use nested dictionaries as the main data structure for storing contact information.

#         Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.

#         Store contact details within the inner dictionary, including:

#             Name

#             Phone number

#             Email address

#             Additional information (e.g., address, notes).



#     Menu Actions:

#         Implement the following actions in response to menu selections:

#             Adding a new contact with all relevant details.

#             Editing an existing contact's information (name, phone number, email, etc.).

#             Deleting a contact by searching for their unique identifier.

#             Searching for a contact by their unique identifier and displaying their details.

#             Displaying a list of all contacts with their unique identifiers.

#             Exporting contacts to a text file in a structured format.

#             Importing contacts from a text file and adding them to the system.



#     User interaction:

#         Utilize input() to enable users to select menu options and provide contact details.

#         Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

#     Error Handling:

#         Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

#     GitHub Repository:

#         Create a GitHub repository for your project.

#         Commit your code to the repository regularly.

#         Create a clean and interactive README.md file in your GitHub repository.

#         include clear instructions on how to run the application and explanations of its features.

#         Provide examples and screenshots, if possible, to enhance user understanding.

#         include a link to your GitHub repository in your project documentation.

#     Optional Bonus Points

#         Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.

#         Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.

#         Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.

#         Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.

#         Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.








# Your task is to develop a Contact Management System with the following features:

#     User interface (UI):

#         Create a user-friendly command-line interface (CLI) for the Contact Management System.

#         Display a welcoming message and provide a menu with the following options:

#         Menu:
#         Add a new contact
#         Edit an existing contact
#         Delete a contact
#         Search for a contact
#         Display all contacts
#         Export contacts to a text file
#         Import contacts from a text file
#         Quit 


#     Contact Data Storage:

#         Use nested dictionaries as the main data structure for storing contact information.

#         Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.

#         Store contact details within the inner dictionary, including:

#             Name

#             Phone number

#             Email address

#             Additional information (e.g., address, notes).

import re

contact_dictionary = {
    "123-456-7890": {
        "Name": "Buzz Lightyear",
        "Phone number": "123-456-7890",
        "Email address": "Buzz@example.com",
        "Additional information": {
            "Address": "123 Elm Street, Springfield",
            "Notes": "Works at Company X",
            "Relationship": "Friend"
        }
    },
    "987-654-3210": {
        "Name": "Zerg Lightyear",
        "Phone number": "987-654-3210",
        "Email address": "zerg@example.com",
        "Additional information": {
            "Address": "456 Oak Street, Springfield",
            "Notes": "Met at conference Y",
            "Relationship": "Foe"
        }
    },
    "719-200-7838": {
        "Name": "Skylar Ennenga",
        "Phone number": "625-263-1920",
        "Email address": "s@example.com",
        "Additional information": "NONE"

    }}

def validate_phone_number(phone_number):
    # Define the regex pattern for 3digits-3digits-4digits
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    # Check if the input matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False


#             Adding a new contact with all relevant details.

def add_contact(contact_dictionary):
    print("Welcome to the add contact page")
    contact_name = input("Lets start with your new contacts phone name: ").capitalize() #Capitalize the first letter of the name
    while True:
        contact_number = input("Lets start with your new contacts phone number: ")
        if validate_phone_number(contact_number): #Verify the phone number is in the correct format
            break
        else:
            print("Invalid phone number, please use the syntax xxx-xxx-xxxx")
    contact_email = input("Lets start with your new contacts phone email: ").capitalize() 
    additional_info = input("Would you like to add any additional information to this contact?: ")
    if additional_info == "1" or additional_info == 'yes': #If the user wants to add additional information
        info_address = input("What is the contacts Address?: ").capitalize()
        info_notes = input("Where did you meet this contact or any other notes?: ").capitalize()
        info_relationship = input("Be them Friend? or Foe!?: ").capitalize()
        
        contact_dictionary.update({contact_number: # Update the dictionary with the new contact
                                {"Name": contact_name, 
                                    "Phone number": contact_number, 
                                    "Email address": contact_email, 
                                    "Additional information": 
                                    {"Address": info_address, 
                                    "Notes": info_notes, 
                                    "Relationship": info_relationship }}})   
    else:
        contact_dictionary.update({contact_number: #Update the dictionary with the new contact
                                {"Name": contact_name, 
                                    "Phone number": contact_number, 
                                    "Email address": contact_email, 
                                    "Additional information": "NONE" # add NONE as a place holder for no additional information
                                    }})  
    

#             Editing an existing contact's information (name, phone number, email, etc.).


def edit_contact(contact_dictionary):
    while True:
        change_contact = input("Please tell the phone number of the contact you would like to update: ")
        if validate_phone_number(change_contact): #Verify the phone number is in the correct format
            break
        else:
            print("Invalid phone number, please use the syntax xxx-xxx-xxxx")
    if change_contact in contact_dictionary: #If the phone number is in the dictionary
        while True:
            print(contact_dictionary[change_contact]["Name"])
            print(contact_dictionary[change_contact]["Phone number"])
            print(contact_dictionary[change_contact]["Email address"])
            entry_change = input(""" Which field are you looking to change?
1. Name 
2. Phone Number
3. Email Address 
4. Additional information 
5. Quit
""")
            
            if entry_change == "1":
                old_name = contact_dictionary[change_contact]["Name"] #Save the old name to print later
                name_change = input("What should we change the name to?: ") #Get the new name
                contact_dictionary[change_contact]["Name"] = name_change #Update the dictionary with the new name
                print(f"Your Name has been changed from {old_name} to {name_change}") #Print the old and new name
                
                
            elif entry_change == "2":
                while True:
                    num_change = input("What should we change the phone number to?: ")
                    if validate_phone_number(num_change): #Verify the phone number is in the correct format
                        break
                    else:
                        print("Invalid phone number, please use the syntax xxx-xxx-xxxx")  #If the phone number is not in the correct format
                old_number = contact_dictionary[change_contact]["Phone number"]
                contact_dictionary[change_contact]["Phone number"] = num_change 
                print(f"Your phone number has been changed from {old_number} to {num_change}")
                
            elif entry_change == "3":
                email_change = input("What should we change the email to?: ")
                old_email = contact_dictionary[change_contact]["Email address"]
                contact_dictionary[change_contact]["Email a4ddress"] = email_change
                print(f"Your phone number has been changed from {old_email} to {email_change}")
                
            elif entry_change == "4":
                if contact_dictionary[change_contact]["Additional information"] == "NONE":
                    print("Looks like you didnt have any Additional information before, you may add it now. ")
                    contact_dictionary[change_contact]["Additional information"] = { # Change additional information so they can manipulate it down below
                                                            "Address": "NONE",
                                                            "Notes": "NONE",
                                                            "Relationship": "NONE"}
                    while True:
                        change_contact_info = input("""What additional information would you like to add?
1. Address
2. Notes
3. Relationship
4. Quit 
""")
                        if change_contact_info == "1":
                            address_info = input("What address would you like to add?: ")
                            contact_dictionary[change_contact]["Additional information"]["Address"] = address_info
                            print(f"{address_info} has been added to your additional information")
                        elif change_contact_info == "2":
                            notes_info = input("What address would you like to add?: ")
                            contact_dictionary[change_contact]["Additional information"]["Notes"] = notes_info
                            print(f"{notes_info} has been added to your additional information")
                        
                        elif change_contact_info == "3":
                            relationship_info = input("What address would you like to add?: ")
                            contact_dictionary[change_contact]["Additional information"]["Relationship"] = relationship_info
                            print(f"{relationship_info} has been added to your additional information")
                        elif change_contact_info == "4":
                            break
                        else:
                            pass
                else:
                    while True:
                        change_contact_info = input("""What additional information would you like to change?
1. Address
2. Notes
3. Relationship
4. Quit 
""")
                        if change_contact_info == "1":
                            address_change = input("What should we change the address to?: ")
                            old_address = contact_dictionary[change_contact]["Additional information"]["Address"]
                            contact_dictionary[change_contact]["Additional information"]["Address"] = address_change
                            print(f"Your Address has been changed from {old_address} to {address_change}")
                        elif change_contact_info == "2":
                            notes_change = input("What should we change the notes to?: ")
                            old_notes = contact_dictionary[change_contact]["Additional information"]["Notes"]
                            contact_dictionary[change_contact]["Additional information"]["Notes"] = notes_change
                            print(f"Your notes has been changed from {old_notes} to {notes_change}")
                        
                        elif change_contact_info == "3":
                            rela_change = input("What should we change the phone Relationship to?: ")
                            old_rela = contact_dictionary[change_contact]["Additional information"]["Relationship"]
                            contact_dictionary[change_contact]["Additional information"]["Relationship"] = rela_change
                            print(f"Your Relationship has been changed from {old_rela} to {rela_change}")
                        elif change_contact_info == "4":
                            break
            elif entry_change == "5":
                break
    else:
        print("Looks like that not in the contact list. Verify you used proper syntax of xxx-xxx-xxxx")
          

#             Deleting a contact by searching for their unique identifier.

def delete_contact(contact_dictionary):
    while True:
        del_choice = input("Please enter the phone number of the contact you would like to delete: ") 
        if validate_phone_number(del_choice): #Verify the phone number is in the correct format
            break
        else:
            print("Invalid phone number, please use the syntax xxx-xxx-xxxx") #If the phone number is not in the correct format
    if del_choice in contact_dictionary: #If the phone number is in the dictionary
            del_contact = contact_dictionary[del_choice] 
            print(f"Name: {del_contact["Name"]}")
            print(f"Phone Number: {del_contact["Phone number"]}")
            print(f"Email Address: {del_contact["Email address"]}")
            confirm_delete = input("Are you sure you would like to delete this contact? ") #Confirm the deletion
            if confirm_delete == "yes" or confirm_delete == "1": #If the user confirms the deletion
                del contact_dictionary[del_choice] #Delete the contact
                print("Contact has been deleted") #Print that the contact has been deleted
            else: #If the user does not confirm the deletion
                print("Contact has not been deleted") #Print that the contact has not been deleted
    else:
        print("Looks like that not in the contact list. Verify you used proper syntax of xxx-xxx-xxxx")  #If the phone number is not in the dictionary    
    pass



#             Searching for a contact by their unique identifier and displaying their details.

def search_contact(contact_dictionary):
    print("Welcome to the search tab")
    while True:
        menu_select = input("""What would you like to do: 
1. Search for a contact 
2. Go back to the main menu?: 
""")
        if menu_select == "1":
            while True:
                contact_search = input("PLease input the phone number of the contact you would like to view.  ")
                if validate_phone_number(contact_search):
                    break
                else:
                    print("Invalid phone number, please use the syntax xxx-xxx-xxxx")
            if contact_search in contact_dictionary: #If the phone number is in the dictionary
                    searched_contact = contact_dictionary[contact_search] #Save the contact to print later
                    print(f"Name: {searched_contact["Name"]}")
                    print(f"Phone Number: {searched_contact["Phone number"]}")
                    print(f"Email Address: {searched_contact["Email address"]}")
                    if searched_contact["Additional information"] == "NONE": #If there is no additional information
                        print("No Additional Information")#Print that there is no additional information
                    else: 
                        print(f"Address: {searched_contact["Additional information"]["Address"]}") 
                        print(f"Notes: {searched_contact["Additional information"]["Notes"]}")
                        print(f"Relationship: {searched_contact["Additional information"]["Relationship"]}")
            else:
                print("Doesnt look like that contact is in you contact list. ")
        elif menu_select == "2": #If the user wants to go back to the main menu
            break
    

#             Displaying a list of all contacts with their unique identifiers.

def display_contact(contact_dictionary):
    for key, value in contact_dictionary.items(): #Print the key and value of the dictionary
        print(f"Name: {value["Name"]}") #
        print(f"Phone Number: {value["Phone number"]}")
        print(f"Email Address: {value["Email address"]}")
        if value["Additional information"] == "NONE": #If there is no additional information
            print("No Additional Information") #Print that there is no additional information
        else:
            print(f"Address: {value["Additional information"]["Address"]}")
            print(f"Notes: {value["Additional information"]["Notes"]}")
            print(f"Relationship: {value["Additional information"]["Relationship"]}")
        
        print("\n")
    

#             Exporting contacts to a text file in a structured format.
def export_contact(contact_dictionary): #Thanks sydney for the help on this one
    file = open("export_contact_list.txt", "w+")  # Opens an entire new file to write in
    with open("export_contact_list.txt", "w") as file:  
        for contact_number, new_contact in contact_dictionary.items(): #For the key and value in the dictionary
            file.write(f"{contact_number}: {new_contact}\n")
    print("Contacts have been exported, please look for the export_contact_list file in your directory! ")
    pass


#             Importing contacts from a text file and adding them to the system.

def import_contact(contact_dictionary):
    try:    
        with open ("import_contact.txt", "r") as file: #Open the file to read
            for line in file: #For each line in the file
                info = line.strip().split() #Strip the line and split it
                phone = info[0] 
                name = info[1] 
                email = info[2]
                address = info[3]
                notes = info[4]
                relationship = info[5]
                
                if phone in contact_dictionary: #If the phone number is in the dictionary
                    print("That contact already in your dictionary") #Print that the contact is already in the dictionary
                else:
                    contact_dictionary.update({phone: {"Name": name, "Phone number": phone, "Email address": email, "Additional information": {"Address": address, "Notes": notes, "Relationship": relationship}}})
                    print("Contact has been added to your dictionary") #Print that the contact has been added to the dictionary
                    print(contact_dictionary)
    except IndexError: #If there is an IndexError - This is to verify there are no hidden lines in the import file
        print("You have recieved and IndexError try verifying there are no hidden lines in the import file.") #Print that there is an IndexError
                    

def main(contact_dictionary):
    while True:
        print("""            
Welcome to the To-Do List App!

Menu:        
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit 
              
              """)
        try:
                # Input for the while loop. 
                menu_item = int(input("What would you like to do? Please input a number 1-8: " ))
                if menu_item == 1: # If the user inputs 1 it will add a contact
                    add_contact(contact_dictionary)
                elif menu_item == 2: # If the user inputs 2 it will edit a contact
                    edit_contact(contact_dictionary)
                elif menu_item == 3: # If the user inputs 3 it will delete a contact
                    delete_contact(contact_dictionary)
                elif menu_item == 4: # If the user inputs 4 it will search for a contact
                    search_contact(contact_dictionary)
                elif menu_item == 5: # If the user inputs 5 it will display all contacts
                    display_contact(contact_dictionary)
                elif menu_item == 6: # If the user inputs 6 it will export the contacts
                    export_contact(contact_dictionary)
                elif menu_item == 7: # If the user inputs 7 it will import the contacts
                    import_contact(contact_dictionary)
                elif menu_item == 8: # If the user inputs 8 it will quit the program
                    break
                else: # If a number outside of 1-8 is chosen it prompts to choose again.
                        print("That's not between 1-8! Try again.")
        except ValueError: # If you print something that cannot become an integer it gives a ValueError which prompts them that its not a number.
                print("That is not a number! ")

main( contact_dictionary)