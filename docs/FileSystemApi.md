# purity_fb.FileSystemApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FileSystemApi.md#create) | **POST** /1.0/file-systems | 
[**list**](FileSystemApi.md#list) | **GET** /1.0/file-systems | 
[**update**](FileSystemApi.md#update) | **PATCH** /1.0/file-systems | 


# **create**
> FileSystemResponse create(filesystem)



Create a new file system

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with given name, provisioned size, and NFS enabled.
    myfs = FileSystem(name="myfs", provisioned="5000", nfs=NfsProtocol(enabled=True))
    try:
        # post the file system object myfs on the array
        res = fb.file_system.create(filesystem=myfs)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filesystem** | [**FileSystem**](FileSystem.md)| the attribute map used to create the file system | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](../README.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> FileSystemResponse list(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List file systems

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException sources=as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all file systems
        fb.file_system.list()
        # list with page size 5, and sort by provisioned in descendant order
        res = fb.file_system.list(limit=5, sort="provisioned-")
        # list all remaining file systems
        res = fb.file_system.list(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.file_system.list(filter='name=\'myfs*\' and nfs.enabled and not(smb.enabled)')
    except rest.ApiException as e:
        print("Exception when listing file systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](../README.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> FileSystemResponse update(name, attributes)



Update an existing file system

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with provisioned size, and NFS enabled
    # note that name field should be None
    new_attr = FileSystem(provisioned="1024", nfs=NfsProtocol(enabled=True), http=ProtocolRule(enabled=False))
    try:
        # update the file system named myfs on the array
        res = fb.file_system.update(name="myfs", attributes=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of the file system to be updated | 
 **attributes** | [**FileSystem**](FileSystem.md)| the new attributes, only modifiable fields could be used. | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](../README.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

