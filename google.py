import json
import os
import re
# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build

class Google:
    def __init__(self):
        self.credentials = None

    def get_credentials(self):
        """
        This function will attempt to find the crednetials.json file in the current directory. If it is not found, it will exit the program.
        """
        try:
            current_dir = os.getcwd()
            filename = os.listdir(current_dir+"/google_credentials")[0] # Assumes only one file in the directory
            if re.match(".*\.json", filename):
                f = open(current_dir+"/google_credentials/"+filename, "r")
                self.credentials = json.load(f)
                f.close()

        except FileNotFoundError:
            print("credentials.json not found. Please place the file in the current directory.")
            exit(1)

    def get_sheet_df(self):
        pass

    # def connect(self):
    #     # Create credentials from the service account key file
    #     credentials = service_account.Credentials.from_service_account_file(
    #         service_account_file, scopes=['https://www.googleapis.com/auth/spreadsheets'])
