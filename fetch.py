from github import Github

# pygithub object
g = Github()


# get repositories of an organization by name
def get_org_repos_by_name(name):
    org = g.get_organization(name)
    print("Organization: ", org.login)
    org_repos = org.get_repos()
    return org_repos


# get all used languages on one organization
def get_all_languages(org_repos):
    languages = list()
    for repo in org_repos:
        if repo.language not in languages:
            languages.append(repo.language)
    return languages


# get the number of used repositories based on used language
def get_lan_num(org_repos, languages):
    lan_num = []
    for lan in languages:
        temp = []
        counter = 0
        temp.append(lan)
        for repo in org_repos:
            if lan == repo.language:
                counter += 1
        temp.append(counter)
        lan_num.append(temp)

    return lan_num


facebook = get_org_repos_by_name("facebook")

print(get_lan_num(facebook, get_all_languages(facebook)))
print(get_all_languages(facebook))
print(len(list(facebook)), " Repos")


twitter = get_org_repos_by_name("twitter")

print(get_lan_num(facebook, get_all_languages(twitter)))
print(get_all_languages(twitter))
print(len(list(twitter)), " Repos")


netflix = get_org_repos_by_name("netflix")

print(get_lan_num(netflix, get_all_languages(netflix)))
print(get_all_languages(netflix))
print(len(list(netflix)), " Repos")


adobe = get_org_repos_by_name("adobe")

print(get_lan_num(adobe, get_all_languages(adobe)))
print(get_all_languages(adobe))
print(len(list(adobe)), " Repos")


#ubuntu = get_org_repos_by_name("ubuntu")

#print(get_lan_num(ubuntu, get_all_languages(ubuntu)))
#print(get_all_languages(ubuntu))
#print(len(list(ubuntu)), " Repos")
