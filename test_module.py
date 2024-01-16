import json
import os
import unittest
from google_interface import Google
from main import get_config


class MyTestCase(unittest.TestCase):
    def test_finds_credentials(self):

        credential_path = os.path.join(os.getcwd(), "google_credentials")

        # Check if the credential file exists
        if len(os.listdir(credential_path)) == 0:
            with open(credential_path + "/credentials.json", "w") as f:  # Create a fake credentials file
                f.write('{"client_id": "123456789"}')
        elif len(os.listdir(credential_path)) > 1:  # Check if there are too many files in the directory
            print("Too many files in google_credentials directory. Please remove all but one file.")
            exit(1)

        # Instantiate Credentials class and test
        creds = Google()
        creds.get_credentials()
        try:
            filename = os.listdir(credential_path)[0]  # Assumes only one file in the directory
            self.assertEqual(os.path.join(os.getcwd(), "google_credentials", filename), creds.credential_file_path)
        finally:
            if os.path.exists(credential_path + "/credentials.json"):
                os.remove(credential_path + "/credentials.json")

    def test_get_sheet_df(self):
        g = Google()
        g.connect()
        sheet_id = "1IeUXt1ZlMQpGBscV5QTEWqxKFOXiH7NK8W5ZmK-xnZk"
        sheet_name = "Sheet1"
        df = g.get_sheet_df(sheet_id, sheet_name)
        print(df.columns)
        # self.assertIsNotNone(df)

    def test_get_config(self):
        config = get_config()
        self.assertEqual(config["sheet_id"], "1IeUXt1ZlMQpGBscV5QTEWqxKFOXiH7NK8W5ZmK-xnZk")




if __name__ == '__main__':
    unittest.main()
