import json
import unittest
import pandas as pd
from main.git_crawler import GitCrawler
import pandas.testing as pd_testing

# from test.base import PyGithubTestCase

"""
class TestUser(PyGithubTestCase):

    def test_username(self):
        user = GitCrawler("octocat")._getting_user()

        with open('./user.json', 'rb') as f:
            expected_body = json.load(f)

        self.assertEqual(user.login, expected_body['login'])  # Tr


    def test_org(self):
        org_details = git_crawler.GitCrawler("OSGeo")._getting_organisation_details()
        sample = git_crawler.GitCrawler("OSGeo")._getting_organisation_details()

        with open('./org.json', 'rb') as f:
            expected_body = json.load(f)
            #repos = int(org_details["number of repositories"][0])

        print(org_details)
        print(sample)
        #self.assertEqual(34, sample)  # Tr
        """


class TestUser1(unittest.TestCase):
    def test_user_name(self):
        user = GitCrawler("sadaffgh")._getting_user()
        self.assertEqual(user.login, 'sadaffgh')

    def test_org_details(self):
        org = "OSGeo"
        data_collected = {
            "organisation": org,
            "number of members": 33,
            "number of repositories": 34,
            "number of languages": 25
        }

        df = pd.DataFrame(data_collected, index=[0])

        pd_testing.assert_frame_equal(df, GitCrawler(org)._getting_organisation_details())

    def test_false_org(self):
        org = "sadaffgh"
        response = 'We have the following problem with "Organisation Details": 404 {"message": "Not Found", ' \
                   '"documentation_url": "https://docs.github.com/rest/reference/orgs#get-an-organization"} '
        assert response
