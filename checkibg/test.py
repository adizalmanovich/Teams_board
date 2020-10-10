import requests
import sys

api_url = sys.argv[1]

def test_get_workers():
    workers = requests.get(url=f"{api_url}/teams")
    if workers.status_code != 200:
        return False
    return True

def test_add_workers():
    workers = requests.post(url=f"{api_url}/teams")
    if workers.status_code != 200:
        return False
    return True






print(test_get_workers())

