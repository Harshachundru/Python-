import requests
r = requests.get("https://opentdb.com/api.php?amount=3&category=22&difficulty=easy&type=multiple")
r.status_code
