import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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

        new_cases_data = data_str.split(",")
                
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
        if len(values) != 3:
            raise ValueError()
    except ValueError:
        print("Invalid input. Please enter a numerical value.\n")
        return False

    return True    


def update_daily_worksheet(data):
    """
    Updates the daily worksheet and adds a new row with the data.
    """
    print("Updating Daily worksheet...\n")
    daily_worksheet = SHEET.worksheet("daily")
    daily_worksheet.append_row(data)
    print("Daily worksheet updated successfully.\n")


def calculate_total_cases(new_cases):
    """
    Calculates the Total number of Active cases by subtracting
    data from Recovered cases and Deaths from New cases.
    """
    print("Calculating Total Active Cases...\n")
    total = SHEET.worksheet("total").get_all_values()
    total_row = total[-1]
    print(total_row)


def main():
    """
    Run all functions.
    """
    data = get_new_cases()
    new_cases_data = [int(num) for num in data]
    update_daily_worksheet(new_cases_data)
    calculate_total_cases(new_cases_data)


main()
