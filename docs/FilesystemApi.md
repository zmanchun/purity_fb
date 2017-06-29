# purity_fb.FilesystemApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FilesystemApi.md#create) | **POST** /1.0/filesystems | 
[**list**](FilesystemApi.md#list) | **GET** /1.0/filesystems | 
[**update**](FilesystemApi.md#update) | **PATCH** /1.0/filesystems | 


# **create**
> FilesystemResponse create(filesystem)



Create a new file system

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.FilesystemApi()
filesystem = purity_fb.FilesystemParam() # FilesystemParam | the attribute map used to create the file system

try: 
    api_response = api_instance.create(filesystem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesystem** | [**FilesystemParam**](FilesystemParam.md)| the attribute map used to create the file system | 

### Return type

[**FilesystemResponse**](FilesystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> FilesystemResponse list(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List file systems

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.FilesystemApi()
names = ['names_example'] # list[str] | A list of names. (optional)
filter = 'filter_example' # str | The filter to be used for query. (optional)
sort = 'sort_example' # str | The way to order the results. (optional)
start = 56 # int | start (optional)
limit = 56 # int | limit (optional)
token = 'token_example' # str | token (optional)

try: 
    api_response = api_instance.list(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**FilesystemResponse**](FilesystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> FilesystemResponse update(attributes, id=id, name=name)



Update an existing file system

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.FilesystemApi()
attributes = purity_fb.FilesystemAttr() # FilesystemAttr | the attribute map to update the file system
id = 'id_example' # str | the ID of the file system to be updated, required if name is not specified (optional)
name = 'name_example' # str | the name of the file system to be updated, required if id is not specified (optional)

try: 
    api_response = api_instance.update(attributes, id=id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | [**FilesystemAttr**](FilesystemAttr.md)| the attribute map to update the file system | 
 **id** | **str**| the ID of the file system to be updated, required if name is not specified | [optional] 
 **name** | **str**| the name of the file system to be updated, required if id is not specified | [optional] 

### Return type

[**FilesystemResponse**](FilesystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

