import requests
from requests.auth import HTTPBasicAuth
import json


# accès à mon compte
username = "diak2021"
token = "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"

# création ddu nouveau dépot
repo_name = "Exam_Api_rest_DIT"
repo_description = "Exercice de simulation"

# lien github
base_url = "https://api.github.com"

# Fonction pour créer un dépôt GitHub
def create_repo():
    url = f"{base_url}/user/repos"
    headers = {"Accept": "application/vnd.github.v3+json"}
    payload = {
        "name": repo_name,
        "description": repo_description,
        "private": False  
    }
    
    response = requests.post(url, headers=headers, auth=HTTPBasicAuth(username, token), json=payload)
    
# Fonction pour créer un ticket (issue) dans le dépôt
def create_issue(repo_full_name, title, body):
    url = f"{base_url}/repos/{repo_full_name}/issues"
    headers = {"Accept": "application/vnd.github.v3+json"}
    payload = {
        "title": title,
        "body": body
    }
    
    response = requests.post(url, headers=headers, auth=HTTPBasicAuth(username, token), json=payload)

# Exécution
if __name__ == "__main__":
    repo_info = create_repo()
    if repo_info:
        repo_full_name = repo_info['full_name']
        
        # Ticekt
        create_issue(repo_full_name, "Ticket 1", "TKT 1")
        create_issue(repo_full_name, "Ticket 2", "TKT 2")