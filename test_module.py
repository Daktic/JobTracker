import os
import unittest
from google import Credentials

class MyTestCase(unittest.TestCase):
    def test_finds_credentials(self):
        # Add fake credentials.json file
        fake_credentials_path = os.path.join(os.getcwd(), "google_credentials", "a.json")

        with open(fake_credentials_path, "w") as f:
            f.write('{"client_id": "123456789"}')

        # Get the list of files and ensure fake credentials file is the first
        files = os.listdir(os.path.join(os.getcwd(), "google_credentials"))
        files.sort()
        files.insert(0, "a.json")

        # Instantiate Credentials class and test
        creds = Credentials()
        creds.get_credentials()
        self.assertEqual('123456789', creds.client_id)  # Test if the client_id is correct

        # Remove fake credentials.json file
        os.remove(fake_credentials_path)

if __name__ == '__main__':
    unittest.main()
