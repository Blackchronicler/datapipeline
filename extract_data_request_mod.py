import requests
from pprint import pprint

# # Getting PAT for auth @ GitHub
f = open("/home/tasongwe/workspace_itech/git/lf8/pat.txt", "r")
pwd_token = f.read()
#print(pwd_token)

## Accessing GitHub User
user = "Blackchronicler"
access_code = pwd_token
r_user = requests.get(f'https://api.github.com/users/{user}', auth=(user, access_code))

print(r_user.status_code, "\n", r_user.raise_for_status(), sep="")
pprint(r_user.json())

## Accessing Github Organisation
payload= {
    "org" : "facebook"
}

r_orga = requests.get("https://api.github.com/orgs/get", params= payload)

print(r_orga.status_code, "\n", r_orga.raise_for_status(), sep="")
pprint(r_orga.json())