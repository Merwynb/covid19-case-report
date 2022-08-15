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
        print("Please enter total number of New cases")
        print("Value should be in numerical format. Example: 33")
        print("Data should be entered ONLY at the end of day i.e. at 22:00\n")

        data_str = input("Enter your data here:")

        print(f"data entered is {data_str} ")

get_new_cases()


