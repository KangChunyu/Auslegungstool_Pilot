import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, filedialog, Button, StringVar, Label
from Input_MaskeConfig import initialize_fields


# Function to dynamically create all input fields
def create_input_fields():
    # Initiate row and column for grid layout
    row = 0
    col = 0

    for label_text, variable in fields.items():
        # Add a header for Energiegbezugsdaten
        if label_text.startswith("Header_"):
            # Extract the text behind the header as the header name
            header_text = label_text.split("_", 1)[1]
            # Move to next row before placing the header
            row += 1
            col = 0
            tk.Label(root, text=header_text, font=('calibre', 12, 'bold')).grid(row=row, column=0, columnspan=4)
            # Move to next row before placing the inputs after headers
            row += 1
            col = 0 
            continue
        
        # Create Dropdown for User Selection
        if label_text in dropdown_options:
            # Create a dropdown(combobox)
            tk.Label(root, text=label_text, font=('calibre', 10, 'bold')).grid(row=row, column=col)
            combo = ttk.Combobox(root, textvariable=variable, values=dropdown_options[label_text], font=('calibre', 10, 'normal'))
            combo.grid(row=row, column=col+1)

        # Create Read-Only Value for User to read first
        elif label_text in predefined_fields:
            # Show the predefined value as a label
            tk.Label(root, text=label_text, font=('calibre', 10, 'bold')).grid(row=row, column=col)
            tk.Label(root, text=predefined_fields[label_text], font=('calibre', 10, 'normal')).grid(row=row, column=col+1)


        # Create User Entry Field for User Input
        else:
            # Create a label for each field
            tk.Label(root, text=label_text, font=('calibre', 10, 'bold')).grid(row=row, column=col)
            # Create an entry widget for each field
            tk.Entry(root, textvariable=variable, font=('calibre', 10, 'normal')).grid(row=row, column=col+1)

        # Alternate between two columns
        if col == 0:
            col = 2
        else:
            col = 0
            row += 1

# Function to retrieve and process input values
def submit_input():
    # Create a new window to display the inputs
    display_window = tk.Toplevel(root)
    display_window.title("User Input Values")
    display_window.geometry("600x400")

    # Display all inputs in the new windows
    row = 0
    # Retrieve the values from the input fields
    for field_name, variable in fields.items():
        value = variable.get()
        tk.Label(display_window, text=f"{field_name}: {value}", font=('calibre', 10, 'normal')).grid(row=row, column=0)
        row += 1


def upload_file(file_type):
    global uploaded_file_path  # Use global variable to store the file path

    # Open a file dialog to select an Excel file
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    if file_path:
        try:
            # Save the file path to the global variable
            uploaded_file_path = file_path
            # Set filetype based on the button clicked


            # Read the Excel file into a DataFrame
            df_input = pd.read_excel(file_path)
            # Convert the first column to datetime
            df_input.iloc[:, 0] = pd.to_datetime(df_input.iloc[:, 0], format='%d.%m.%Y %H:%M', errors='coerce')
            # Convert the second column to numeric
            df_input.iloc[:, 1] = pd.to_numeric(df_input.iloc[:, 1], errors='coerce')

            # Save the file seprately depends on the filetype
            if file_type == "Kundendaten":
                temp_file_path = "uploaded_Kundendaten.csv"
            elif file_type == "BHKW":
                temp_file_path = "uploaded_BHKW.csv"
            elif file_type == "PV":
                temp_file_path = "uploaded_PV.csv"
                
            else:
                raise ValueError("Invalid file type specified. Use 'Kundendaten' or 'BHKW' or 'PV'.")

            # Save the DataFrame to a temporary CSV file
            df_input.to_csv(temp_file_path, index=False)
            messagebox.showinfo("Success", f"Data loaded successfully and saved to {temp_file_path}!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Creating a button for uploading files (kundendaten or BHKW)
def create_upload_button(row, file_type):
    button_text = f"Upload {file_type} File"
    upload_btn = tk.Button(root, text=button_text, command=lambda: upload_file(file_type))
    upload_btn.grid(row=row, column=1)


###########################################################################################################################################

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

# Initialize fields and predefined fields
fields, predefined_fields, dropdown_options = initialize_fields()

# Create input fields dynamically
create_input_fields()

# Create the upload button for Input Kundendaten
create_upload_button(row=len(fields) + 2, file_type="Kundendaten")

# Create the upload button for BHKW
create_upload_button(row=len(fields) + 3, file_type="BHKW")

# Create the upload button for PV
create_upload_button(row=len(fields) + 4, file_type="PV")

# Create a button for submitting and upload the input file
submit_btn = tk.Button(root, text="Submit", command=submit_input)
submit_btn.grid(row=len(fields) + 5, column=1)

# Performing infinite loop for the window to display
root.mainloop()
