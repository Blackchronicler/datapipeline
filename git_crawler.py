from secrets import token_bytes
import requests
from pprint import pprint
from github import Github

class Git_Crawler:
        
    ## Getting PAT for auth @ GitHub
    with open("/home/tasongwe/workspace_itech/git/lf8/pat.txt", "r") as f:
        access_tokens = f.readlines()
        user_token = access_tokens[0]
        pwd_token = access_tokens[1]
        #print(user, pwd_token, sep="")

    # Instantiating GitHub
    g = Github(login_or_token= user_token, password= pwd_token)

    def __init__(self, git_entity) -> None:
            self.git_entity = git_entity

    def _getting_user(self):
        """ Extracting the necessary user information from GitHub """
        
        try:
            user = self.g.get_user(self.git_entity)
            print(f"The User\'s name is: {user.name}")

        except Exception as e:
            print(f"We have the following problem with \"User Name\": {str(e)}")
            
    def _getting_organisation_details(self):
        """
        Extracting the necessary organisational data 
        (languages, repositories and more) from GitHub
        
        """
        
        try:       
            languages_used = {}
            orga = self.g.get_organization(self.git_entity)
            #print(f"The following Organisation exists: {orga.login}")
            members = list(orga.get_members(filter_="all"))
            print(f"The Organisation has: {len(members)} members.")
            repos = list(orga.get_repos(type= "all", sort= "full_name"))
            #print(f"The Organisation has: {len(repos)} repositories.")
            
            for repo in repos[:5]:
                langs_used = repo.get_languages()
                for language in langs_used:
                    if language not in languages_used:
                        languages_used[language] = langs_used[language] 
                    else:
                        languages_used[language] = (languages_used[language] + langs_used[language])
            pprint(languages_used) 
                
        except Exception as e:
            print(f'We have the following problem with \"Organisation Name\": {str(e)}')


if __name__ == "__main__":
    Git_Crawler("blackchronicler")._getting_user()
    Git_Crawler("OSGeo")._getting_organisation_details()