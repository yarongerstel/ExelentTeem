import requests
import time
import datetime
from collections import namedtuple


class Datajob():
    def __init__(self, data, list_category=[], list_kaywords=[]):
        self.datajobs = requests.get(data).json()
        self._date = int(time.time())
        self._search_keywords = list_kaywords
        self._search_categories = list_category

    """
        Searches in the API the jobs with the given ID number, when they are after the date entered
        :return a list of namedtuple jobs that meet the requirements
    """

    def get_job_by_id(self, job_id):
        lis = []
        for job in self.datajobs:
            if job["job_id"] == str(job_id):
                # Converts the posting_date to datetime and then converts it to epoch time
                datejob = datetime.datetime.strptime(job["posting_date"], '%Y-%m-%dT%H:%M:%S.000').timestamp()
                if self._date < datejob:  # Checks if work time after search time
                    lis.append(
                        namedtuple('job', job.keys())(**job))  # If so converts to namedtuple and puts in the list
        # If the list contains more than one element another list returns a dictionary
        if len(lis) > 1:
            return lis
        return dict(lis)

    """
        Search the API for jobs with a date later than the date entered
        :return a list of namedtuple jobs that meet the requirements
    """

    def list_jobs_posted_after(self):
        lis = []
        for job in self.datajobs:
            # Converts the posting_date to datetime and then converts it to epoch time
            datejob = datetime.datetime.strptime(job["posting_date"], '%Y-%m-%dT%H:%M:%S.000').timestamp()
            # Checks if work time after search time
            if self._date < datejob:
                lis.append(namedtuple('job', job.keys())(**job))  # If so converts to namedtuple and puts in the list
        return lis

    """
        Search in the API the jobs with the categories entered in self._search_categories
        :return a list of namedtuple jobs that meet the requirements
    """

    def list_by_categories(self):
        lis = []
        for job in self.datajobs:
            if "job_category" in job.keys():  # For each job make sure it has a category
                # For any job that has a category, look in the category list if there is a match if so, add to the list
                for category in self._search_categories:
                    if category == job["job_category"]:
                        lis.append(namedtuple('job', job.keys())(**job))
                        break
        return lis

    """
        Search in the API the jobs with the keywords entered in self._search_keywords
        :returns a list of namedtuple of jobs that meet the requirements
    """

    def list_by_keywords(self):
        lis = []
        # For each job search in the keyword list if there is a match then add to the list
        for job in self.datajobs:
            for key in self._search_keywords:
                if key in job["business_title"] or key in job["job_description"]:
                    lis.append(namedtuple('job', job.keys())(**job))
                    break
        return lis

