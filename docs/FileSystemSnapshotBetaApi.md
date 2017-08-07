# purity_fb.FileSystemSnapshotBetaApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](FileSystemSnapshotBetaApi.md#delete) | **DELETE** /beta/file-system-snapshots |


# **delete**
> delete(name)



Delete a file system snapshot by name

### Example
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28

try:
res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
print("Exception when logging in to the array: %sn" % e)
if res:
try:
# delete a file system snapshot named myfs.mysnap
fb.file_system_snapshot_beta.delete(name="myfs.mysnap")
except rest.ApiException as e:
print("Exception when deleting file system snapshots: %sn" % e)
```

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
**name** | **str**| name of the file system snapshot to be deleted |

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](README.md#AuthTokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

