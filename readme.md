# Contact Management Application

Welcome to the Contact Management Application! This Python program allows you to manage a contact list with functionalities to add, edit, delete, search, display, export, and import contacts. 

## Features

1. **Add a New Contact**: Add a new contact with a name, phone number, email, and optional additional information (address, notes, relationship).
2. **Edit an Existing Contact**: Modify the details of an existing contact, including name, phone number, email, and additional information.
3. **Delete a Contact**: Remove a contact from the contact list by providing their phone number.
4. **Search for a Contact**: Search for a contact by phone number and display their details.
5. **Display All Contacts**: Display the list of all contacts along with their details.
6. **Export Contacts**: Export the contact list to a text file.
7. **Import Contacts**: Import contacts from a text file and add them to the contact list.

## Usage

1. **Add a New Contact**:
    - Follow the prompts to enter the contact's name, phone number, and email.
    - Optionally, add additional information such as address, notes, and relationship status.

2. **Edit an Existing Contact**:
    - Enter the phone number of the contact you want to edit.
    - Follow the prompts to update the contact's details.

3. **Delete a Contact**:
    - Enter the phone number of the contact you want to delete.
    - Confirm the deletion when prompted.

4. **Search for a Contact**:
    - Enter the phone number of the contact you want to search for.
    - The contact's details will be displayed if found.

5. **Display All Contacts**:
    - View the list of all contacts and their details.

6. **Export Contacts**:
    - Export the contact list to a text file named `export_contact_list.txt`.

7. **Import Contacts**:
    - Import contacts from a text file named `import_contact.txt`.

## Functions

### `validate_phone_number(phone_number)`

Validates if the phone number is in the format `xxx-xxx-xxxx`.

### `add_contact(contact_dictionary)`

Adds a new contact to the contact dictionary.

### `edit_contact(contact_dictionary)`

Edits the details of an existing contact in the contact dictionary.

### `delete_contact(contact_dictionary)`

Deletes a contact from the contact dictionary by phone number.

### `search_contact(contact_dictionary)`

Searches for a contact by phone number and displays their details.

### `display_contact(contact_dictionary)`

Displays all contacts and their details.

### `export_contact(contact_dictionary)`

Exports the contact list to a text file.

### `import_contact(contact_dictionary)`

Imports contacts from a text file and adds them to the contact dictionary.

### `main(contact_dictionary)`

Main function to run the application, providing a menu to access all features.

Follow the prompts to interact with the application.

Feel free to contribute to the project by opening issues or submitting pull requests. Happy coding!