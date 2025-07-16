import tkinter as tk
from Input_Maske import initialize_fields, create_input_fields, create_upload_button, submit_input
from Ergebnisse import Energiefluesse, Engergiebezugsdaten


def run_input_maske():
    """
    Run the Input_Maske GUI to collect user input and uploaded files.
    """

    # Initialize fields and predefined fields
    global fields, predefined_fields, dropdown_options
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

    # Run the tkinter main loop
    root.mainloop()

    # Return the collected fields for further processing
    return fields


def perform_calculations(fields):
    """
    Perform calculations using the collected data.
    """
    print("Performing calculations...")

    # Calculate Energiefluesse
    print("Calculating Energiefluesse...")
    energie_fluesse = Energiefluesse()
    print("Energiefluesse calculated successfully.")

    # Calculate Energiebezugsdaten
    print("Calculating Energiebezugsdaten...")
    energie_bezugsdaten = Engergiebezugsdaten(fields)
    print("Energiebezugsdaten calculated successfully.")

    return energie_fluesse, energie_bezugsdaten


def display_results(energie_fluesse, energie_bezugsdaten):
    """
    Display the results in the console or a GUI.
    """
    print("\nEnergiefluesse:")
    for key, value in energie_fluesse.items():
        print(f"{key}: {value}")

    print("\nEnergiebezugsdaten:")
    for key, value in energie_bezugsdaten.items():
        print(f"{key}: {value}")


if __name__ == "__main__":

    # Create a tkinter root window
    root = tk.Tk()
    root.geometry("800x600")


    # Run Input_Maske to collect user input and uploaded files
    collected_fields = run_input_maske(root)

    # Perform calculations using the collected data
    energie_fluesse, energie_bezugsdaten = perform_calculations(collected_fields)

    # Display the results
    display_results(energie_fluesse, energie_bezugsdaten)