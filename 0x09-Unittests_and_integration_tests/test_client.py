#!/usr/bin/env python3
""" client unittesting Module """


from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


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
