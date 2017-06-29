# purity_fb.FilesystemBetaApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](FilesystemBetaApi.md#delete) | **DELETE** /beta/filesystems | 


# **delete**
> FilesystemResponse delete(name=name)



delete a file system by name

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.FilesystemBetaApi()
name = 'name_example' # str | name of the file system to be deleted (optional)

try: 
    api_response = api_instance.delete(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemBetaApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system to be deleted | [optional] 

### Return type

[**FilesystemResponse**](FilesystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

