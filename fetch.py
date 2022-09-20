import base64
from github import Github
from pprint import pprint

# Github username
username = "x4nth055"
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-" * 50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    # try:
    # repo license
    # print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    # except:
    # pass


# search by programming language
def find_py_repos():
    #    for i, repo in enumerate(g.search_repositories("language:python")):
    #        print_repo(repo)
    #        print("=" * 100)
    #        if i == 9:
    #            break

    # enumerate_py = enumerate(g.search_repositories("language:python"))
    # print(len(list(enumerate_py)))

    org = g.get_organization("PyGithub")
    print(org.login)

    repositories = list(g.search_repositories(query='language:python'))
    len_repo = len(repositories)
    for repo in repositories:
        print(len_repo)


# for repo in user.get_repos():
#    print_repo(repo)


find_py_repos()
