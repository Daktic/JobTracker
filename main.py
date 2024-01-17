import json
from application import JobList
from google_interface import Google
import pandas as pd


def get_config():
    with open("config.json", "r") as f:
        return json.load(f)


class App():
    def __init__(self):
        self.job_df = None
        self.joblist = JobList()
        self.config = get_config()
        self.google_interface = Google(self.config['sheet_id'], self.config['sheet_name'])

    def calculate_metrics(self):
        self.job_df = self.google_interface.get_sheet_df()
        self.calculate_response_times()
        self.calculate_job_titles()
        self.calculate_company_stats()

    def calculate_response_times(self):
        """
        This will look at the response time in days column and run some stats on it
        """
        # Get the columns
        response_time_col = self.job_df["Response Time(DAYS)"]
        # Convert to numeric
        response_time_col.replace("No Response Yet", '', inplace=True)
        response_time_col = response_time_col.apply(pd.to_numeric)
        # Calculate response time metrics
        total_apps = len(response_time_col)
        num_responses = sum(response_time_col.notnull())
        print(f"Of the {total_apps} jobs, {num_responses} have responded. "
              f"{round(total_apps / num_responses, 2)}%")
        # print out the data types of each value
        print(f"\nOf those {num_responses}:")
        print(f"Average response time: {round(response_time_col.mean(), 1)} Days")
        print(f"Median response time: {response_time_col.median()} Days")

    def calculate_job_titles(self):
        """
        This will look at the job type column and run some stats on it
        """
        # Get the columns
        job_type_col = self.job_df["Title"]
        # Calculate job type metrics
        distinct_counts = job_type_col.value_counts()
        print(f"\nThere are {len(distinct_counts)} distinct job Titles")
        print(f"Top 5 :{distinct_counts.head(5)}")

    def calculate_company_stats(self):
        """
        This will look at the company column and run some stats on it
        """
        # Get the columns
        company_col = self.job_df["Company"]
        # Calculate company metrics
        distinct_counts = company_col.value_counts()
        print(f"\nThere are {len(distinct_counts)} distinct companies")
        print(f"Top 5 :{distinct_counts.head(5)}")


if __name__ == "__main__":
    app = App()
    app.calculate_metrics()
