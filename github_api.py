# import needed modules
import requests
#import black
from datetime import date

#-------------------------------------------------------------------------
# Function that retrieves pull request with - repository name, start date
# and end date as arguments
#-------------------------------------------------------------------------
def github_pull(repo_name, start_date, end_date):
    pull_requests = requests.get(f"https://api.github.com/repos/Umuzi-org/tech-department/pulls?id=37012297")
    my_request = pull_requests.json()
    return my_requests

# repos = {
#     "id": 37012297,
#     "created_at": "2020-04-20T11:23:53Z",
#     "updated_at": "2020-04-20T11:23:53Z",
# }