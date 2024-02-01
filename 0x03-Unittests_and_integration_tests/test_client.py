#!/usr/bin/env python3
"""This module defines class TestGithubOrgClient"""

from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GithubOrgClient(org_name)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @patch('client.get_json')
    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result, mock_json):
        """ Test method returns correct output """
        mock_json.return_value = {'repos_url': 'http://some_url.com'}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Unit-test GithubOrgClient.public_repos"""
        payload = [{
            "name": "repo1",
            "html_url": "https://github.com/org/repo1"
            },
            {
            "name": "repo2",
            "html_url": "https://github.com/org/repo2"
            }]
        mock_json.return_value = payload
        with patch("client.GithubOrgClient._public_repos_url",
                   PropertyMock(
                       return_value="https://github.com/org/repos"
                       )) as mock_public_repos_url:
            instance = GithubOrgClient('org')
            repos = instance.public_repos()
            self.assertEqual(repos, payload)
            mock_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Unit-test GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)
