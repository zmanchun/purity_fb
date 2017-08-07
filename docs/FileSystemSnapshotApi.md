# purity_fb.FileSystemSnapshotApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FileSystemSnapshotApi.md#create) | **POST** /1.0/file-system-snapshots | 
[**list**](FileSystemSnapshotApi.md#list) | **GET** /1.0/file-system-snapshots | 


# **create**
> FileSystemSnapshotResponse create(sources, suffix=suffix)



Create snapshots for the specified source filesystems

### Example 
```python
from purity_fb import PurityFb, SnapshotSuffix, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # create a snapshot for the file system named myfs
        res = fb.file_system_snapshot.create(sources=["myfs"])
        print(filesystem_snap_response)
        # create a snapshot with suffix mysnap for the file system named myfs
        res = fb.file_system_snapshot.create(sources=["myfs"], suffix=SnapshotSuffix("mysnap"))
        print(filesystem_snap_response)
    except rest.ApiException as e:
        print("Exception when creating file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources** | [**list[str]**](str.md)| a list of names of source file systems | 
 **suffix** | [**SnapshotSuffix**](SnapshotSuffix.md)| the suffix of the snapshot | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list**
> FileSystemSnapshotResponse list(filter=filter, sort=sort, start=start, limit=limit, token=token, names_or_sources=names_or_sources)



List file system snapshots

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException sources=as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all file system snapshots
        fb.file_system_snapshot.list()
        # list with page size 5, and sort by source file system name
        res = fb.file_system_snapshot.list(limit=5, sort="source")
        # list all remaining file system snapshots
        res = fb.file_system_snapshot.list(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.file_system_snapshot.list(filter='source=\'myfs*\' and contains(suffix, \'1\')')
    except rest.ApiException as e:
        print("Exception when listing file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **names_or_sources** | [**list[str]**](str.md)| a list of names of snapshots or source file systems | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

