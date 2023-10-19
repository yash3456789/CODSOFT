# Contact Book Application
# This Python application provides a GUI for managing contact information, including names, phone numbers, emails, and addresses.

# Features:
# - Add, view, update, and delete contact details.
# - Search for contacts by name or phone number.
# - Stylish GUI with clear labeling and easy interaction.

# How It Works:
# 1. Add Contact: Enter contact details and click "Add Contact" to save.
# 2. View Contacts: Display a list of all saved contacts.
# 3. Search: Find contacts by name or phone number.
# 4. Update Contact: Modify existing contact details by selecting contact and input details in respective fields then click update.
# 5. Delete Contact: Remove a selected contact.


import tkinter as tk
from tkinter import messagebox

# Create a class for the Contact Book application


class ContactBookApp:
    def __init__(self, root):
        # Initialize the ContactBookApp
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []  # List to store contact information

        # Create and configure the widgets for the GUI
        self.create_gui()

    def create_gui(self):
        # Create and configure the graphical user interface (GUI) elements

        # Title Label
        self.title_label = tk.Label(
            self.root, text="Contact Book", font=("Arial", 18))
        self.title_label.pack(pady=10)

        # Frame for Input Fields
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        # Entry Fields for Contact Details
        entry_width = 30  # Set a common width for all entry fields

        # Labels and Entry Fields for Name, Phone, Email, and Address
        self.name_label = tk.Label(input_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame, width=entry_width)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(input_frame, text="Phone:")
        self.phone_label.grid(row=0, column=2, padx=5, pady=5)
        self.phone_entry = tk.Entry(input_frame, width=entry_width)
        self.phone_entry.grid(row=0, column=3, padx=5, pady=5)

        self.email_label = tk.Label(input_frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(input_frame, width=entry_width)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.address_label = tk.Label(input_frame, text="Address:")
        self.address_label.grid(row=1, column=2, padx=5, pady=5)
        self.address_entry = tk.Entry(input_frame, width=entry_width)
        self.address_entry.grid(row=1, column=3, padx=5, pady=5)

        # Button to Add a Contact
        self.add_button = tk.Button(
            self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)

        # Search Functionality
        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.root, width=entry_width)
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(
            self.root, text="Search", command=self.search_contact)
        self.search_button.pack()

        # Listbox to Display Contacts
        self.contact_listbox = tk.Listbox(
            self.root, width=entry_width * 2, height=10)
        self.contact_listbox.pack(pady=10)

        self.view_contacts_button = tk.Button(
            self.root, text="View Contacts", command=self.view_contacts)
        self.view_contacts_button.pack()

        # Buttons for Various Actions
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)  # Add spacing

        # Update Contact Button
        self.update_button = tk.Button(
            button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side=tk.LEFT, padx=5)

        # Delete Contact Button (Colored Red)
        self.delete_button = tk.Button(
            button_frame, text="Delete Contact", command=self.delete_contact, fg="red")
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_contact(self):
        # Get contact details from input fields
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Check if name and phone are provided
        if name and phone:
            contact = {"Name": name, "Phone": phone,
                       "Email": email, "Address": address}
            self.contacts.append(contact)  # Add the contact to the list
            self.clear_entry_fields()  # Clear input fields
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror(
                "Error", "Name and a valid phone number are required fields.")

    def clear_entry_fields(self):
        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        # Clear the search entry field
        self.search_entry.delete(0, tk.END)

        # Display all contacts in the listbox
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            contact_info = f"{contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}"
            self.contact_listbox.insert(tk.END, contact_info)

    def search_contact(self):
        # Search for contacts by name or phone number and display in the listbox
        query = self.search_entry.get().lower()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query in contact["Name"].lower() or query in contact["Phone"]:
                contact_info = f"{contact['Name']} - {contact['Phone']} - {contact['Email']} - {contact['Address']}"
                self.contact_listbox.insert(tk.END, contact_info)

    def update_contact(self):
        # Update the selected contact with new details
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            # Check if name or phone or email or address is provided
            if name or phone or email or address:
                if name:
                    self.contacts[selected_index]["Name"] = name
                if phone:
                    self.contacts[selected_index]["Phone"] = phone
                if email:
                    self.contacts[selected_index]["Email"] = email
                if address:
                    self.contacts[selected_index]["Address"] = address

                self.clear_entry_fields()
                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror(
                    "Error", "Enter at least one field to update.")
        else:
            messagebox.showerror("Error", "Select a contact to update.")

    def delete_contact(self):
        # Delete the selected contact
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            del self.contacts[selected_index]
            self.clear_entry_fields()
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Select a contact to delete.")


if __name__ == "__main__":
    # Create the main window for the application
    root = tk.Tk()

    # Create an instance of the ContactBookApp class, passing the main window as the root
    app = ContactBookApp(root)

    # Start the main event loop, allowing the application to respond to user interactions
    root.mainloop()
