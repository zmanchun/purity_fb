# coding: utf-8

"""
    FlashBlade Management API

    The management APIs of FlashBlade.

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import purity_fb
from purity_fb.rest import ApiException
from purity_fb.models.http_rule import HttpRule


class TestHttpRule(unittest.TestCase):
    """ HttpRule unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHttpRule(self):
        """
        Test HttpRule
        """
        model = purity_fb.models.http_rule.HttpRule()


if __name__ == '__main__':
    unittest.main()
