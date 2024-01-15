import datetime
import pandas as pd
from enum import Enum


class JobList:
    """
    This class should hold the data responsible for translating job details into the Google Sheet
    From here you can do crud operations like adding, deleting, and updating a record.
    """

    def __init__(self):
        self.jobs = []

    # Add a job to the job tracker
    def add_job(self, company: str, title: str, locations: [str], site: str):
        new_job = Job(company, title, locations, site)
        self.jobs.append(new_job)

    # Convert the joblist into a dataframe, this makes it easier to upload to google
    def to_df(self):
        df = pd.DataFrame()

        for job in self.jobs:
            job_line = [
                job.application.application_date,
                job.company,
                job.title,
                job.locations.join(", "),
                job.site,
                job.application.response_date,
                job.application.status_code
            ]
            df = df.append(job_line, ignore_index=True)

    def from_df(self, df: pd.DataFrame):
        for index, row in df.iterrows():
            self.add_job(row["Company"], row["Title"], row["Locations"].split(", "), row["Site"])


# For updating status on the application
class Status(Enum):
    Pending = "Pending"
    Accepted = "Accepted"
    Rejected = "Rejected"


class Job:
    """
    The Job identifies characteristics about the job itself. It also creates new applications from the job.
    """

    def __init__(self, company: str, title: str, locations: [str], site: str) -> None:
        self.company = company
        self.title = title
        self.locations = locations
        self.site = site
        self.application = self.create_application()

    def create_application(self):
        return Application()

    def record_response(self, status: Status):
        self.application.update_status(status)


class Application:
    """
    The Application creates a timestamp of its creation and sets the application status as pending.
    It can be modified to reflect new information in status and response date.
    """

    def __init__(self):
        self.application_date = datetime.datetime.now()
        self.status = Status.Pending
        self.response_date = None

    def update_status(self, status: Status):
        self.status = status
        self.response_date = datetime.datetime.now()
