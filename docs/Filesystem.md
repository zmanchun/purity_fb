# Filesystem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the a (or reference to a) file system or snapshot | 
**fast_remove_enabled** | **bool** | is fast remove mode enabled? | [optional] 
**nfs** | [**NfsRule**](NfsRule.md) | NFS configuration | [optional] 
**http** | [**HttpRule**](HttpRule.md) | HTTP configuration | [optional] 
**smb** | [**ProtocolRule**](ProtocolRule.md) | SMB configuration | [optional] 
**filesystem_id** | **str** | the id of the file system | [optional] 
**created** | **int** | the time when the file system is created | [optional] 
**snapshots_enabled** | **bool** | are snapshots enabled? | [optional] 
**as_of** | **int** | the time when the file system is created | [optional] 
**space** | [**FilesystemSpace**](FilesystemSpace.md) | the space specification of the file system | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


