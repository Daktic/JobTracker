import json
import os
import unittest
from google import Credentials


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
        creds = Credentials()
        creds.get_credentials()
        try:
            filename = os.listdir(credential_path)[0]  # Assumes only one file in the directory
            f = open(os.path.join(credential_path, filename), "r")
            cred_json = json.load(f)
            client_id = cred_json["client_id"]
            self.assertEqual(client_id, creds.client_id)
            f.close()
        finally:
            if os.path.exists(credential_path + "/credentials.json"):
                os.remove(credential_path + "/credentials.json")


if __name__ == '__main__':
    unittest.main()
