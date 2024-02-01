#!/usr/bin/env python3
"""Test the utils module."""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """This class tests the fuction for Nested Map"""
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map function."""
        with self.assertRaises(KeyError) as e:
            wrong = access_nested_map(nested_map, path)
            self.assertEqual(wrong, str(e.exception))


class TestGetJson(unittest.TestCase):
    """Class for testing get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, test_payload):
        """Test for get_json method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            payload = get_json(url)
            self.assertEqual(payload, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class for testing memoization"""

    def test_memoize(self):
        """ Tests memoize function """
        class TestClass:
            """ Test class"""
            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test_case = TestClass()
            test_case.a_property
            test_case.a_property
            mocked.asset_called_once()
