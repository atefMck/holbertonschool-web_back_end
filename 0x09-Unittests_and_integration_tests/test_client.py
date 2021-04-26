#!/usr/bin/env python3
""" client unittesting Module """


from client import GithubOrgClient
import unittest
from unittest.mock import patch
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
