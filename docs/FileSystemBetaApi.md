# purity_fb.FileSystemBetaApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](FileSystemBetaApi.md#delete) | **DELETE** /beta/file-systems |


# **delete**
> delete(name)



Delete a file system by name

### Example
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
print("Exception when logging in to the array: %sn" % e)
if res:
try:
# delete a file system with name myfs
fb.file_system_beta.delete(name="myfs")
except rest.ApiException as e:
print("Exception when deleting file system: %sn" % e)
```

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**name** | **str**| name of the file system to be deleted |

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#documentation-for-api-endpoints) [[Back to Model list]](index.md#documentation-for-models) [[Back to README]](index.md)

