
import os
import re

import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build


class Google:
    def __init__(self, sheet_id: str, sheet_name: str):
        self.credential_file_path = None
        self.sheet_service = None
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name

    def get_sheet_df(self):
        self._connect()
        return self._retrieve_sheet_df(self.sheet_id, self.sheet_name)

    def _get_credentials(self):
        """
        This function will attempt to find the crednetials.json file in the current directory. If it is not found, it will exit the program.
        """
        try:
            current_dir = os.getcwd()
            self.credential_file_path = os.path.join(current_dir,"google_credentials", os.listdir(current_dir + "/google_credentials")[0])  # Assumes only one file in the directory

        except FileNotFoundError:
            print("credentials.json not found. Please place the file in the current directory.")
            exit(1)

    def _retrieve_sheet_df(self, sheet_id: str, sheet_name: str):
        """
        This function will get the sheet from the Google Sheet and return it as a dataframe
        """
        # Call the Sheets API
        sheet = self.sheet_service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=sheet_name).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return None
        else:
            return pd.DataFrame(values[1:], columns=values[0])

    def _connect(self):
        # If credentials is None, get the credentials
        if self.credential_file_path is None:
            self._get_credentials()
        # Create credentials from the service account key file
        credentials = service_account.Credentials.from_service_account_file(
            self.credential_file_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])

        self.sheet_service = build('sheets', 'v4', credentials=credentials)
