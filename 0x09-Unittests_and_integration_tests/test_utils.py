#!/usr/bin/env python3
""" unittesting Module """

from typing import Mapping, Sequence
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ access_nested_map unit testing class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, res):
        """ access_nested_map result testing method """
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence):
        """ access_nested_map exceptions testing method """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
