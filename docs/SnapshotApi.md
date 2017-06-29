# purity_fb.SnapshotApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SnapshotApi.md#create) | **POST** /1.0/filesystem-snapshots | 
[**list**](SnapshotApi.md#list) | **GET** /1.0/filesystem-snapshots | 


# **create**
> SnapshotResponse create(sources=sources, suffix=suffix)



create snapshots for the specified source filesystems

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.SnapshotApi()
sources = ['sources_example'] # list[str] | a list of names of source file systems (optional)
suffix = purity_fb.SnapshotSuffix() # SnapshotSuffix | the suffix of the snapshot (optional)

try: 
    api_response = api_instance.create(sources=sources, suffix=suffix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources** | [**list[str]**](str.md)| a list of names of source file systems | [optional] 
 **suffix** | [**SnapshotSuffix**](SnapshotSuffix.md)| the suffix of the snapshot | [optional] 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> SnapshotResponse list(filter=filter, sort=sort, start=start, limit=limit, token=token, names_or_sources=names_or_sources)



List snapshots

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.SnapshotApi()
filter = 'filter_example' # str | The filter to be used for query. (optional)
sort = 'sort_example' # str | The way to order the results. (optional)
start = 56 # int | start (optional)
limit = 56 # int | limit (optional)
token = 'token_example' # str | token (optional)
names_or_sources = ['names_or_sources_example'] # list[str] | a list of names of snapshots or source file systems (optional)

try: 
    api_response = api_instance.list(filter=filter, sort=sort, start=start, limit=limit, token=token, names_or_sources=names_or_sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit | [optional] 
 **token** | **str**| token | [optional] 
 **names_or_sources** | [**list[str]**](str.md)| a list of names of snapshots or source file systems | [optional] 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

