# coding: utf-8

"""
    FlashBlade Management API

    The management APIs of FlashBlade.

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from environment import HOST, API_TOKEN
from purity_fb import *
import purity_fb


class TestAuthenticationApi(unittest.TestCase):
    """ AuthenticationApi unit test stubs """

    def setUp(self):
        self.purity_fb = PurityFb(HOST)

    def tearDown(self):
        pass

    def test_auth(self):
        """
        Test case for authentication

        
        """
        res = self.purity_fb.login(api_token=API_TOKEN)
        self.assertTrue(res == 200)

        self.purity_fb.file_system.list()
        self.purity_fb.file_system_snapshot.list()

        res = self.purity_fb.logout()
        self.assertTrue(res == 200)

        with self.assertRaises(purity_fb.rest.ApiException) as context:
            self.purity_fb.file_system.list()
        self.assertTrue('Forbidden' in str(context.exception))

        with self.assertRaises(purity_fb.rest.ApiException) as context:
            self.purity_fb.logout()
        self.assertTrue('Forbidden' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
