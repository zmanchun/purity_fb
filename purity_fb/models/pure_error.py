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


class PureError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, pure_err_code=None, pure_err_context=None, pure_err_key=None, pure_err_msg=None):
        """
        PureError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'int',
            'pure_err_code': 'int',
            'pure_err_context': 'str',
            'pure_err_key': 'str',
            'pure_err_msg': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'pure_err_code': 'pure_err_code',
            'pure_err_context': 'pure_err_context',
            'pure_err_key': 'pure_err_key',
            'pure_err_msg': 'pure_err_msg'
        }

        self._code = code
        self._pure_err_code = pure_err_code
        self._pure_err_context = pure_err_context
        self._pure_err_key = pure_err_key
        self._pure_err_msg = pure_err_msg

    @property
    def code(self):
        """
        Gets the code of this PureError.
        error code

        :return: The code of this PureError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this PureError.
        error code

        :param code: The code of this PureError.
        :type: int
        """

        self._code = code

    @property
    def pure_err_code(self):
        """
        Gets the pure_err_code of this PureError.
        pure error code

        :return: The pure_err_code of this PureError.
        :rtype: int
        """
        return self._pure_err_code

    @pure_err_code.setter
    def pure_err_code(self, pure_err_code):
        """
        Sets the pure_err_code of this PureError.
        pure error code

        :param pure_err_code: The pure_err_code of this PureError.
        :type: int
        """

        self._pure_err_code = pure_err_code

    @property
    def pure_err_context(self):
        """
        Gets the pure_err_context of this PureError.
        pure error context

        :return: The pure_err_context of this PureError.
        :rtype: str
        """
        return self._pure_err_context

    @pure_err_context.setter
    def pure_err_context(self, pure_err_context):
        """
        Sets the pure_err_context of this PureError.
        pure error context

        :param pure_err_context: The pure_err_context of this PureError.
        :type: str
        """

        self._pure_err_context = pure_err_context

    @property
    def pure_err_key(self):
        """
        Gets the pure_err_key of this PureError.
        pure error key

        :return: The pure_err_key of this PureError.
        :rtype: str
        """
        return self._pure_err_key

    @pure_err_key.setter
    def pure_err_key(self, pure_err_key):
        """
        Sets the pure_err_key of this PureError.
        pure error key

        :param pure_err_key: The pure_err_key of this PureError.
        :type: str
        """

        self._pure_err_key = pure_err_key

    @property
    def pure_err_msg(self):
        """
        Gets the pure_err_msg of this PureError.
        pure error message

        :return: The pure_err_msg of this PureError.
        :rtype: str
        """
        return self._pure_err_msg

    @pure_err_msg.setter
    def pure_err_msg(self, pure_err_msg):
        """
        Sets the pure_err_msg of this PureError.
        pure error message

        :param pure_err_msg: The pure_err_msg of this PureError.
        :type: str
        """

        self._pure_err_msg = pure_err_msg

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
        if not isinstance(other, PureError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
