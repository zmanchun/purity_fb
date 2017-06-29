# coding: utf-8

"""
    FlashBlade Management API

    The management APIs of FlashBlade.

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FilesystemResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, items=None, pagination_info=None):
        """
        FilesystemResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'items': 'list[Filesystem]',
            'pagination_info': 'PaginationInfo'
        }

        self.attribute_map = {
            'items': 'items',
            'pagination_info': 'pagination_info'
        }

        self._items = items
        self._pagination_info = pagination_info

    @property
    def items(self):
        """
        Gets the items of this FilesystemResponse.

        :return: The items of this FilesystemResponse.
        :rtype: list[Filesystem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this FilesystemResponse.

        :param items: The items of this FilesystemResponse.
        :type: list[Filesystem]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def pagination_info(self):
        """
        Gets the pagination_info of this FilesystemResponse.
        paging information

        :return: The pagination_info of this FilesystemResponse.
        :rtype: PaginationInfo
        """
        return self._pagination_info

    @pagination_info.setter
    def pagination_info(self, pagination_info):
        """
        Sets the pagination_info of this FilesystemResponse.
        paging information

        :param pagination_info: The pagination_info of this FilesystemResponse.
        :type: PaginationInfo
        """
        if pagination_info is None:
            raise ValueError("Invalid value for `pagination_info`, must not be `None`")

        self._pagination_info = pagination_info

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
        if not isinstance(other, FilesystemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
