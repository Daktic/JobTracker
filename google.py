import json
import os
import re


class Google:
    def __init__(self):
        self.client_id = None

    def get_credentials(self):
        """
        This function will attempt to find the crednetials.json file in the current directory. If it is not found, it will exit the program.
        """
        try:
            current_dir = os.getcwd()
            filename = os.listdir(current_dir+"/google_credentials")[0] # Assumes only one file in the directory
            if re.match(".*\.json", filename):
                f = open(current_dir+"/google_credentials/"+filename, "r")
                cred_json = json.load(f)
                self.client_id = cred_json["client_id"]
                f.close()

        except FileNotFoundError:
            print("credentials.json not found. Please place the file in the current directory.")
            exit(1)