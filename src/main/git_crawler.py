from github import Github
import pandas as pd


class GitCrawler:
    ## Getting PAT for auth @ GitHub
    """
    with open("../../pat.txt", "r") as f:
        access_tokens = f.readlines()
        user_token = access_tokens[0]
        pwd_token = access_tokens[1]
        # print(user, pwd_token, sep="")

    # Instantiating GitHub
    g = Github(login_or_token=user_token, password=pwd_token)
    """

    g = Github()

    def __init__(self, git_entity: str) -> None:
        self.git_entity = git_entity

    def _getting_user(self):
        """ Extracting the necessary user information from GitHub """

        try:
            user = self.g.get_user(self.git_entity)
            return user

        except Exception as e:
            return f"We have the following problem with \"User Name\": {str(e)}"

    def _getting_languages_used(self):
        """ Getting all programming languages being used in the organisation """
        try:
            orga = self.g.get_organization(self.git_entity)
            repos = list(orga.get_repos(type="all", sort="full_name"))
            languages_used = {}
            for repo in repos[:5]:
                langs_used = repo.get_languages()
                for language in langs_used:
                    if language not in languages_used:
                        languages_used[language] = langs_used[language]
                    else:
                        languages_used[language] = (languages_used[language] + langs_used[language])
            df = pd.DataFrame(list(languages_used.items()), columns=["language_typ", "bytes"])
            df["organisation_name"] = [orga.login for _ in range(len(df))]

        except Exception as e:
            print(f'We have the following problem with \"Organisation Languages\": {str(e)}')

        return df

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
            # cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
            #           (orga_name, len(repos), len(members)))
            # conn.commit()

            df = pd.DataFrame(data_collected)
            return df

        except Exception as e:
            return f'We have the following problem with \"Organisation Details\": {str(e)}'


if __name__ == "__main__":
    # Git_Crawler("blackchronicler")._getting_user()
    sample = GitCrawler("OSGeo")._getting_organisation_details()
    print(sample)
