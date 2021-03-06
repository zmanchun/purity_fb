# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API 1.0, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/en/latest/).

    OpenAPI spec version: 1.0
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FileSystemSnapshotApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create(self, sources, **kwargs):
        """
        Create snapshots for the specified source filesystems
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(sources, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sources: a list of names of source file systems (required)
        :param SnapshotSuffix suffix: the suffix of the snapshot
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(sources, **kwargs)
        else:
            (data) = self.create_with_http_info(sources, **kwargs)
            return data

    def create_with_http_info(self, sources, **kwargs):
        """
        Create snapshots for the specified source filesystems
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(sources, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] sources: a list of names of source file systems (required)
        :param SnapshotSuffix suffix: the suffix of the snapshot
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sources', 'suffix']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sources' is set
        if ('sources' not in params) or (params['sources'] is None):
            raise ValueError("Missing the required parameter `sources` when calling `create`")


        collection_formats = {}

        resource_path = '/1.0/file-system-snapshots'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'sources' in params:
            query_params['sources'] = params['sources']
            collection_formats['sources'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'suffix' in params:
            body_params = params['suffix']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileSystemSnapshotResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list(self, **kwargs):
        """
        List file system snapshots
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param str sort: The way to order the results.
        :param int start: start
        :param int limit: limit, should be >= 0
        :param str token: token
        :param list[str] names_or_sources: a list of names of snapshots or source file systems
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        List file system snapshots
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: The filter to be used for query.
        :param str sort: The way to order the results.
        :param int start: start
        :param int limit: limit, should be >= 0
        :param str token: token
        :param list[str] names_or_sources: a list of names of snapshots or source file systems
        :return: FileSystemSnapshotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'sort', 'start', 'limit', 'token', 'names_or_sources']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/1.0/file-system-snapshots'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'token' in params:
            query_params['token'] = params['token']
        if 'names_or_sources' in params:
            query_params['names_or_sources'] = params['names_or_sources']
            collection_formats['names_or_sources'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['AuthTokenHeader']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FileSystemSnapshotResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
