
# Project Requirements

# Your task is to develop a Contact Management System with the following features:

#     User Interface (UI):

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



#     User Interaction:

#         Utilize input() to enable users to select menu options and provide contact details.

#         Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

#     Error Handling:

#         Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

#     GitHub Repository:

#         Create a GitHub repository for your project.

#         Commit your code to the repository regularly.

#         Create a clean and interactive README.md file in your GitHub repository.

#         Include clear instructions on how to run the application and explanations of its features.

#         Provide examples and screenshots, if possible, to enhance user understanding.

#         Include a link to your GitHub repository in your project documentation.

#     Optional Bonus Points

#         Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.

#         Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.

#         Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.

#         Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.

#         Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.








# Your task is to develop a Contact Management System with the following features:

#     User Interface (UI):

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
    }, }
#     Menu Actions:

#         Implement the following actions in response to menu selections:

#             Adding a new contact with all relevant details.

def add_contact(contact_dictionary):
    print("Welcome to the add contact page")
    contact_name = input("Lets start with your new contacts phone name: ").capitalize()
    contact_number = input("Lets start with your new contacts phone number: ")
    contact_email = input("Lets start with your new contacts phone email: ").capitalize()
    additional_info = input("Would you like to add any additional information to this contact?: ")
    if additional_info == "1" or additional_info == 'yes':
        # add_info = input("What aditional info would you like to add?: ") Potentially add different options
        info_address = input("What is the contacts Address?: ").capitalize()
        info_notes = input("Where did you meet this contact or any other notes?: ").capitalize()
        info_relationship = input("Be them Friend? or Foe!?: ").capitalize()
        
        contact_dictionary.update({contact_number: 
                                   {"Name": contact_name, 
                                    "Phone Number": contact_number, 
                                    "Email Address": contact_email, 
                                    "Additional information": 
                                    {"Address": info_address, 
                                     "Notes": info_notes, 
                                     "Relationship": info_relationship }}})   
    else:
        contact_dictionary.update({contact_number: 
                                   {"Name": contact_name, 
                                    "Phone Number": contact_number, 
                                    "Email Address": contact_email, 
                                    "Additional information": "NONE" 
                                     }})  
    print(contact_dictionary)
add_contact(contact_dictionary)




#             Editing an existing contact's information (name, phone number, email, etc.).

def edit_contact():
    pass

#             Deleting a contact by searching for their unique identifier.
def delete_contact():
    # Needs to search for a specific unique identifier.
    pass

#             Searching for a contact by their unique identifier and displaying their details.
def search_contact():
    pass

#             Displaying a list of all contacts with their unique identifiers.

def display_contact():
    pass

#             Exporting contacts to a text file in a structured format.
def export_contact():
    pass

#             Importing contacts from a text file and adding them to the system.

def import_contact():
    pass



