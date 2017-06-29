# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API 1.0, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/en/latest/).

    OpenAPI spec version: 1.0
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FileSystem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, created=None, nfs=None, http=None, smb=None, fast_remove_directory_enabled=False, provisioned=0, snapshot_directory_enabled=False, space=None):
        """
        FileSystem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'created': 'int',
            'nfs': 'NfsRule',
            'http': 'ProtocolRule',
            'smb': 'ProtocolRule',
            'fast_remove_directory_enabled': 'bool',
            'provisioned': 'int',
            'snapshot_directory_enabled': 'bool',
            'space': 'Space'
        }

        self.attribute_map = {
            'name': 'name',
            'created': 'created',
            'nfs': 'nfs',
            'http': 'http',
            'smb': 'smb',
            'fast_remove_directory_enabled': 'fast_remove_directory_enabled',
            'provisioned': 'provisioned',
            'snapshot_directory_enabled': 'snapshot_directory_enabled',
            'space': 'space'
        }

        self._name = name
        self._created = created
        self._nfs = nfs
        self._http = http
        self._smb = smb
        self._fast_remove_directory_enabled = fast_remove_directory_enabled
        self._provisioned = provisioned
        self._snapshot_directory_enabled = snapshot_directory_enabled
        self._space = space

    @property
    def name(self):
        """
        Gets the name of this FileSystem.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this FileSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileSystem.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this FileSystem.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this FileSystem.
        creation timestamp of the object

        :return: The created of this FileSystem.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this FileSystem.
        creation timestamp of the object

        :param created: The created of this FileSystem.
        :type: int
        """

        self._created = created

    @property
    def nfs(self):
        """
        Gets the nfs of this FileSystem.
        NFS configuration. Modifiable.

        :return: The nfs of this FileSystem.
        :rtype: NfsRule
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this FileSystem.
        NFS configuration. Modifiable.

        :param nfs: The nfs of this FileSystem.
        :type: NfsRule
        """

        self._nfs = nfs

    @property
    def http(self):
        """
        Gets the http of this FileSystem.
        HTTP configuration. Modifiable.

        :return: The http of this FileSystem.
        :rtype: ProtocolRule
        """
        return self._http

    @http.setter
    def http(self, http):
        """
        Sets the http of this FileSystem.
        HTTP configuration. Modifiable.

        :param http: The http of this FileSystem.
        :type: ProtocolRule
        """

        self._http = http

    @property
    def smb(self):
        """
        Gets the smb of this FileSystem.
        SMB configuration. Modifiable.

        :return: The smb of this FileSystem.
        :rtype: ProtocolRule
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """
        Sets the smb of this FileSystem.
        SMB configuration. Modifiable.

        :param smb: The smb of this FileSystem.
        :type: ProtocolRule
        """

        self._smb = smb

    @property
    def fast_remove_directory_enabled(self):
        """
        Gets the fast_remove_directory_enabled of this FileSystem.
        is fast remove directory enabled? Modifiable.

        :return: The fast_remove_directory_enabled of this FileSystem.
        :rtype: bool
        """
        return self._fast_remove_directory_enabled

    @fast_remove_directory_enabled.setter
    def fast_remove_directory_enabled(self, fast_remove_directory_enabled):
        """
        Sets the fast_remove_directory_enabled of this FileSystem.
        is fast remove directory enabled? Modifiable.

        :param fast_remove_directory_enabled: The fast_remove_directory_enabled of this FileSystem.
        :type: bool
        """

        self._fast_remove_directory_enabled = fast_remove_directory_enabled

    @property
    def provisioned(self):
        """
        Gets the provisioned of this FileSystem.
        the provisioned size of the file system in bytes. Modifiable

        :return: The provisioned of this FileSystem.
        :rtype: int
        """
        return self._provisioned

    @provisioned.setter
    def provisioned(self, provisioned):
        """
        Sets the provisioned of this FileSystem.
        the provisioned size of the file system in bytes. Modifiable

        :param provisioned: The provisioned of this FileSystem.
        :type: int
        """

        self._provisioned = provisioned

    @property
    def snapshot_directory_enabled(self):
        """
        Gets the snapshot_directory_enabled of this FileSystem.
        is snapshot directory enabled? Modifiable.

        :return: The snapshot_directory_enabled of this FileSystem.
        :rtype: bool
        """
        return self._snapshot_directory_enabled

    @snapshot_directory_enabled.setter
    def snapshot_directory_enabled(self, snapshot_directory_enabled):
        """
        Sets the snapshot_directory_enabled of this FileSystem.
        is snapshot directory enabled? Modifiable.

        :param snapshot_directory_enabled: The snapshot_directory_enabled of this FileSystem.
        :type: bool
        """

        self._snapshot_directory_enabled = snapshot_directory_enabled

    @property
    def space(self):
        """
        Gets the space of this FileSystem.
        the space specification of the file system

        :return: The space of this FileSystem.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this FileSystem.
        the space specification of the file system

        :param space: The space of this FileSystem.
        :type: Space
        """

        self._space = space

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FileSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
