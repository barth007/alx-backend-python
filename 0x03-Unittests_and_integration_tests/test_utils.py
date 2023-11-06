#!/usr/bin/env python3
"""
test_utils.py
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
# from unittest.mock import patch
from typing import (
    Mapping,
    Sequence,
    Any
)


class TestAccessNestedMap(unittest.TestCase):
    """
    A test class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            input: Mapping,
            path: Sequence, expected: Any):
        """
        A simple test method to return expected outcome
        """

        self.assertEqual(access_nested_map(input, path), expected)
