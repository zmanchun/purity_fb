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


class HttpRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, enabled=False, require_ssl=True):
        """
        HttpRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'require_ssl': 'bool'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'require_ssl': 'require_ssl'
        }

        self._enabled = enabled
        self._require_ssl = require_ssl

    @property
    def enabled(self):
        """
        Gets the enabled of this HttpRule.
        is the protocol enabled?

        :return: The enabled of this HttpRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this HttpRule.
        is the protocol enabled?

        :param enabled: The enabled of this HttpRule.
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")

        self._enabled = enabled

    @property
    def require_ssl(self):
        """
        Gets the require_ssl of this HttpRule.
        is ssl required?

        :return: The require_ssl of this HttpRule.
        :rtype: bool
        """
        return self._require_ssl

    @require_ssl.setter
    def require_ssl(self, require_ssl):
        """
        Sets the require_ssl of this HttpRule.
        is ssl required?

        :param require_ssl: The require_ssl of this HttpRule.
        :type: bool
        """

        self._require_ssl = require_ssl

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
        if not isinstance(other, HttpRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
