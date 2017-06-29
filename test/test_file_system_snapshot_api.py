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


def assert_is_snapshot_list(items):
    assert type(items) is list
    for item in items:
        assert type(item) is FileSystemSnapshot

FS_A = 'rest_client_fs_for_snap_a'
FS_B = 'rest_client_fs_for_snap_b'

DEBUG = False

class TestFileSystemSnapshotApi(unittest.TestCase):
    """ SnapshotsApi unit test stubs """

    def setUp(self):
        self.purity_fb = PurityFb(HOST)
        res = self.purity_fb.login(API_TOKEN)
        self.assertTrue(res == 200)
        self.file_system = self.purity_fb.file_system
        self.file_system_beta = self.purity_fb.file_system_beta
        self.snapshot = self.purity_fb.file_system_snapshot
        self.snapshot_beta = self.purity_fb.file_system_snapshot_beta
        self.cleanUp()
        fsa = FileSystem(name=FS_A)
        fsb = FileSystem(name=FS_B)
        self.file_system.create(filesystem=fsa)
        self.file_system.create(filesystem=fsb)

    def tearDown(self):
        self.cleanUp()
        self.purity_fb.logout()

    def cleanUp(self):
        filter = 'name=\"' + FS_A + '*\" or name=\"' + FS_B + '*\"'
        res = self.file_system.list(filter=filter)
        for fs in res.items:
            self.file_system_beta.delete(name=fs.name)
        # deleting a file system will delete its snapshots
        # so no need to clean up snapshots

    def test_create(self):
        """
        Test case for create
        """
        response = self.snapshot.create(sources=[FS_A])
        assert type(response) is FileSystemSnapshotResponse
        assert_is_snapshot_list(response.items)
        assert len(response.items) == 1
        assert response.items[0].source == FS_A

        suffix = "snap-by-sdk"
        response = self.snapshot.create(sources=[FS_A], suffix=SnapshotSuffix(suffix=suffix))
        assert type(response) is FileSystemSnapshotResponse
        assert_is_snapshot_list(response.items)
        assert len(response.items) == 1
        assert response.items[0].source == FS_A
        assert response.items[0].suffix == suffix


    def test_list(self):
        """
        Test case for list
        """
        suffix = "snap-by-sdk"
        self.snapshot.create(sources=[FS_A], suffix=SnapshotSuffix(suffix=suffix))
        self.snapshot.create(sources=[FS_B], suffix=SnapshotSuffix(suffix=suffix))

        response = self.snapshot.list()
        if DEBUG:
            print (response)
        assert type(response) is FileSystemSnapshotResponse
        assert_is_snapshot_list(response.items)

        response = self.snapshot.list(names_or_sources=[FS_A])
        assert type(response) is FileSystemSnapshotResponse
        assert_is_snapshot_list(response.items)
        for snapshot in response.items:
            assert snapshot.source == FS_A
            assert snapshot.name.startswith(FS_A + '.')

        snap_name = "%s.%s" % (FS_B, suffix)
        response = self.snapshot.list(names_or_sources=[FS_A, snap_name])
        assert type(response) is FileSystemSnapshotResponse
        assert_is_snapshot_list(response.items)
        for snapshot in response.items:
            assert snapshot.name == snap_name or snapshot.source == FS_A


if __name__ == '__main__':
    unittest.main()
