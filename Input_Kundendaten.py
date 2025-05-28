import pandas as pd

# Define a function to read the temporary file as a DataFrame
def read_temp_file(file_path):
    try:
        # Read the temporary CSV file into a DataFrame
        df = pd.read_csv(file_path)
        print("DataFrame loaded successfully from temporary file!")
        # Display the first few rows of the DataFrame
        print(df.head())  
        return df
    except FileNotFoundError:
        print("No temporary file found. Please upload a file first.")
        return None
    except Exception as e:
        print(f"Error reading the temporary file: {str(e)}")
        return None


# Load the Dataframe at the module level
kundendaten_file_path = "uploaded_Kundendaten.csv"
bhkw_file_path = "uploaded_BHKW.csv"
pv_file_path = "uploaded_PV.csv"

kundendaten_df = read_temp_file(kundendaten_file_path)
bhkw_df = read_temp_file(bhkw_file_path)
pv_df = read_temp_file(pv_file_path)
