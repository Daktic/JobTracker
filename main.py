import json
from application import JobList
from google_interface import Google

def get_config():
    with open("config.json", "r") as f:
        return json.load(f)


class App():
    def __init__(self):
        self.joblist = JobList()
        self.config = get_config()
        self.google_interface = Google(self.config['sheet_id'], self.config['sheet_name'])

    def calculate_metrics(self):
        g = self.google_interface.get_sheet_df()
        print(g)


    def calculate_response_times(self):
        pass






if __name__ == "__main__":
    app = App()
    app.calculate_metrics()
