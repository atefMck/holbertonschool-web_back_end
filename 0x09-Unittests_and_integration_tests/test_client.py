#!/usr/bin/env python3
""" client unittesting Module """


from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ GithubOrgClient unittesting class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, org, patched):
        """ GithubOrgClient.org unittesting """

        test_class = GithubOrgClient(org)
        self.assertEqual(test_class.org, patched.return_value)
        patched.assert_called_once()

    def test_public_repos_url(self):
        """ GithubOrgClient._public_repos_url unittesting """

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value={'repos_url': 'http://bigBrain.url'}
                   ) as patched:
            test_class = GithubOrgClient("BigBrain")
            result = test_class._public_repos_url
            self.assertEqual(result, patched.return_value['repos_url'])

    @patch('client.get_json',
           return_value={'repos_url': 'http://bigBrain.url'})
    def test_public_repos(self, first_patch):
        """ GithubOrgClient.public_repos unittesting """

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=[]
                   ) as second_patch:
            test_class = GithubOrgClient("BigBrain")
            result = test_class.public_repos(license="SmallBrain")
            self.assertEqual(result, second_patch.return_value)
            first_patch.assert_called_once()
            second_patch.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, has_license):
        """ GithubOrgClient.has_license unittesting """

        test_class = GithubOrgClient("BigBrain")
        self.assertEqual(test_class.has_license(repo, license),
                         has_license)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ GithubOrgClient integration testing class """

    @classmethod
    def setUpClass(self):
        """ GithubOrgClient integration testing patcher setup """
        self.get_patcher = patch('requests.get',
                                 side_effect=[self.org_payload,
                                              self.repos_payload])
        self.get_patcher.start()

    @classmethod
    def tearDownClass(self):
        """ GithubOrgClient integration testing patcher destroy """
        self.get_patcher.stop()
    
    def test_public_repos(self):
        """ GithubOrgClient integration testing public_repos """
        test_class = GithubOrgClient("BigBrain")
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)