import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('covid19-case-report')


def get_new_cases():
    """
    Get New cases data from user.
    """
    while True:
        print("Please enter total number of New cases.")
        print("Value should be in numerical format. Example: 33")
        print("Data should be entered ONLY at the end of day i.e. at 22:00\n")

        data_str = input("Enter New Cases: ")

        new_cases_data = data_str.split(" ")
        
        if validate_data(new_cases_data):
            print("Thank You for your input.\n")
            break

    return new_cases_data    


def validate_data(values):
    """
    converts string into integers and checks to confirm 
    user enters an Integer and will keep asking until 
    user enters a valid input.
    """
    try:
        [int(value) for value in values]
        if len(values) > 1:
            raise ValueError()
    except ValueError:
        print("Invalid input. Please enter a numerical value.\n")
        return False

    return True    


def update_new_cases_column(new_cases):
    """
    Updates the daily worksheet and adds a new row with the data.
    """
    print("Updating Daily worksheet...\n")
    new_cases_column = SHEET.worksheet("daily")
    new_cases_column.append_row(new_cases)
    print("Daily worksheet updated successfully.\n")


data = get_new_cases()
new_cases_data = [int(num) for num in data]
update_new_cases_column(new_cases_data)
