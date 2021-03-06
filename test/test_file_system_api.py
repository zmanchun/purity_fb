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


DEMO_LIST = 'test_list'
DEMO_CREATE = 'test_create'
PUSER ='pureuser'
FS_COUNT = 5
DEBUG = False


def print_list(items):
    if items:
        print('[')
        for item in items:
            print(item)
        print(']')


def dl_name(i):
    return DEMO_LIST + str(i)


def dc_name(i):
    return DEMO_CREATE + str(i)


def check_is_filesystem_list(list):
    if list:
        for item in list:
            assert type(item) is FileSystem, 'seen type {}'.format(type(item))


def list_by_filter(api, filter_str):
    print ('Filter: {}...\n'.format(filter_str))
    res = api.list(filter=filter_str)
    if DEBUG:
        print_list(res.items)
    check_is_filesystem_list(res.items)
    return res


def list_and_sort(api, sort_key):
    print ('\nSORT by {}'.format(sort_key))
    res = api.list(sort=sort_key, limit=10)
    if DEBUG:
        print_list(res.items)
    check_is_filesystem_list(res.items)
    return res


def list_by_start(api, start_key):
    print ('\nSTART by {}'.format(start_key))
    res = api.list(start=start_key)
    if DEBUG:
        print_list(res.items)
    check_is_filesystem_list(res.items)
    return res


def list_by_limit(api, limit_key):
    print ('\nLIMIT is {}'.format(limit_key))
    res = api.list(limit=limit_key, _return_http_data_only="False")
    if DEBUG:
        print_list(res.items)
    check_is_filesystem_list(res.items)
    return res


def list_by_token(api, token_key):
    print ('\nTOKEN is {}'.format(token_key))
    res = api.list(token=token_key)
    if DEBUG:
        print_list(res.items)
    check_is_filesystem_list(res.items)
    return res


class TestFileSystemApi(unittest.TestCase):
    """ FileSystemsApi unit test stubs """

    def setUp(self):
        self.purity_fb = PurityFb(HOST)
        res = self.purity_fb.login(API_TOKEN)
        self.assertTrue(res == 200)
        self.file_system = self.purity_fb.file_system
        self.file_system_beta = self.purity_fb.file_system_beta
        self.cleanUp()
        for i in range(FS_COUNT):
            fs = FileSystem()
            fs.name = DEMO_LIST + '%d' % i
            fs.nfs = NfsRule(enabled=True)
            fs.provisioned = 1000
            self.file_system.create(filesystem=fs)
            fs.name = DEMO_CREATE + '%d' % i
            self.file_system.create(filesystem=fs)

    def tearDown(self):
        self.cleanUp()
        self.purity_fb.logout()

    def cleanUp(self):
        filter = 'name=\"' + DEMO_LIST + '*\" or name=\"' + DEMO_CREATE + '*\"'
        res = self.file_system.list(filter=filter)
        for fs in res.items:
            attr = FileSystem()
            attr.nfs = NfsRule(enabled=False)
            attr.http = ProtocolRule(enabled=False)
            attr.smb = ProtocolRule(enabled=False)
            self.file_system.update(name=fs.name, attributes=attr)
            self.file_system_beta.delete(name=fs.name)

    def test_list_basic(self):
        print('LIST all file systems\n')
        res = self.file_system.list(limit=50)
        if DEBUG:
            print_list(res.items)
        check_is_filesystem_list(res.items)

        names = [dl_name(0), dl_name(1)]
        print('\nLIST file systems by names {}\n'.format(names))
        res = self.file_system.list(names=names)
        if DEBUG:
            print_list(res.items)

        filter_str = 'name = \'' + DEMO_LIST + '*\''
        print('\nLIST file systems by filter {}\n'.format(filter_str))
        res = self.file_system.list(filter=filter_str)
        if DEBUG:
            print_list(res.items)
        check_is_filesystem_list(res.items)

        print('\nCREATE file system {}\n'.format(DEMO_CREATE))
        fs = FileSystem()
        fs.name = DEMO_CREATE
        fs.provisioned = "300000"
        try:
            res = self.file_system.create(filesystem=fs)
        except:
            pass
        if DEBUG:
            print_list(res.items)
        check_is_filesystem_list(res.items)

    def test_filter(self):
        # ----------- test FILTER ------------
        print ('\nLIST file system by filters\n')

        filter_str = 'name = \'' + DEMO_CREATE + '*\''
        list_by_filter(self.file_system, filter_str)

        filter_str = 'name = \'' + DEMO_LIST + '*\' and not(contains(name, \'2\'))' + ' and created > 1456000'
        list_by_filter(self.file_system, filter_str)

    def test_sort(self):
        # ------ test SORT ----
        print ('\nLIST file system and sort\n')
        list_and_sort(self.file_system, 'name')
        list_and_sort(self.file_system, '(natural)')
        list_and_sort(self.file_system, 'name-')
        list_and_sort(self.file_system, 'provisioned')
        list_and_sort(self.file_system, 'provisioned-')
        list_and_sort(self.file_system, 'smb.enabled')

    def test_start(self):
        # ------ test START ----
        print ('\nLIST file system by start\n')
        list_by_start(self.file_system, 1)
        list_by_start(self.file_system, 2)

    def demo_limit(self):
        # ------ demo LIMIT ----
        input('\nEnter to list file system by limit\n')
        list_by_limit(self.file_system, 0)
        list_by_limit(self.file_system, 1)
        list_by_limit(self.file_system, 2)
        list_by_limit(self.file_system, 5)

    def test_token(self):
        # ------ demo TOKEN ----
        print ('\nLIST file system by token\n')
        res = list_by_limit(self.file_system, 1)
        token = res.pagination_info.continuation_token
        list_by_token(self.file_system, token)

    def test_combined(self):
        print ('\nLIST file system by combined parameters\n')
        print ('\nLIST by start, limit, filter\n')
        res = self.file_system.list(start=1, limit=3, filter='name = \'' + DEMO_CREATE + '*\'')
        if DEBUG:
            print_list(res.items)
        check_is_filesystem_list(res.items)

    def test_update(self):
        name = DEMO_CREATE + '0'
        size = 10000
        fs_attr = FileSystem()
        fs_attr.provisioned = size
        res = self.file_system.update(name=name, attributes=fs_attr)
        check_is_filesystem_list(res.items)
        updated_fs = res.items[0]
        self.assertTrue(updated_fs.name == name)
        self.assertTrue(updated_fs.provisioned == size)


if __name__ == '__main__':
    unittest.main()
