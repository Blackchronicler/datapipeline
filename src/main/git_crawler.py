from github import Github
import pandas as pd


class GitCrawler:
    
    # Instantiating GitHub
    g = Github()

    def __init__(self, git_entity: str) -> None:
        self.git_entity = git_entity

    def _getting_user(self):
        """ Extracting the necessary user information from GitHub """

        try:
            user = self.g.get_user(self.git_entity)
            return (f"The User\'s name is: {user.name}")

        except Exception as e:
            print(f"We have the following problem with \"User Name\": {str(e)}")
            exit(1)

    def _getting_languages_used(self):
        
        """ Getting all programming languages being used in the organisation """
        try:
            org = self.g.get_organization(self.git_entity)
            repos = list(org.get_repos(type="all", sort="full_name"))
            languages_used = {}
            for repo in repos[:5]:
                langs_used = repo.get_languages()
                for language in langs_used:
                    if language not in languages_used:
                        languages_used[language] = langs_used[language] 
                    else:
                        languages_used[language] = (languages_used[language] + langs_used[language])
            df = pd.DataFrame(list(languages_used.items()), columns=["language_typ", "bytes"])
            df["organisation_name"] = [org.login for _ in range(len(df))]
            return df

        except Exception as e:
            print(f'We have the following problem with \"Organisation Languages\": {str(e)}')
            exit(1)


    def _getting_organisation_details(self):
        """
        Extracting the necessary organisational data 
        (languages, repositories and more) from GitHub
        
        """
        try:
            orga = self.g.get_organization(self.git_entity)
            orga_name = orga.login
            members = list(orga.get_members(filter_="all"))
            repos = list(orga.get_repos(type="all", sort="full_name"))
            data_collected = {
                "organisation": [orga_name],
                "number of members": [len(members)],
                "number of repositories": [len(repos)],
                "number of languages": [len(self._getting_languages_used())]
            }
            
            df = pd.DataFrame(data_collected)
            return df

        except Exception as e:
            print(f'We have the following problem with \"Organisation Details\": {str(e)}')
            exit(1)
