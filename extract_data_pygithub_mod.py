import requests
from pprint import pprint
from github import Github

## Instantiating GitHub
g = Github()

def getting_user(names):
    try:
        ## Getting user name
        user = g.get_user(names)
        print(f"The User\'s name is: {user.name}")

    except Exception as e:
        print(f"We have the following problem with \"User Name\": {str(e)}")
        
def confirm_organisation(name):
    try:
        ## Getting organisation name
        orga = g.get_organization(name)
        print(f"The following Organisation exists: {orga.login}")

    except Exception as e:
        print(f"We have the following problem with \"Organisation Name\": {str(e)}")
        
        


if __name__ == "__main__":
    getting_user("steph-omi")  #test
    confirm_organisation("netflix")  #test