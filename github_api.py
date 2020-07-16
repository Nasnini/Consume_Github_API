# import needed modules
import requests
from datetime import date
import urllib3
import os
from github import Github

# Retrieving authorization token from my_config file
user =os.environ.get("USER")
token =os.environ.get("TOKEN")
github_user(user, password)

#-------------------------------------------------------------------------
# Function that retrieves pull request with - repository name, start date
# and end date as arguments
#-------------------------------------------------------------------------
def github_pull(repo_name:str, start_date:str, end_date:str):
    repo =g.get_repo("Umuzi.org/{repo_url}")
    pulls = repo.get_pulls(state='open', sort='createc_at', base='master')
    for pr in pulls:
        if pr.createc_at == start_date and pr.closed_at == end_date:
            pull_requests = {
                "Date Created at" : pr.createc_at,
                "Date Updated at" : pr.updated_at,
                "Date Merged at" : pr.mergerd_at,
                "Date Closed at" : pr.closed_at,
                "repo" : pr.review_comments
            }
        print(pull_requests)

if __name__ == "__main__":
    start_date = date(2020, 5, 3)
    end_date = date(2020, 7, 15)
    print(github_pull("Theo-Kobuoe-190-rabbitmq", start_date, end_date))





    # pull_requests = requests.get(f"https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=37012297")
    # my_request = pull_requests.json()
    # print my_request

