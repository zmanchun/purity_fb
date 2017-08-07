# FileSystem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional]
**created** | **int** | creation timestamp of the object | [optional]
**nfs** | [**NfsRule**](NfsRule.md) | NFS configuration. Modifiable. | [optional]
**http** | [**ProtocolRule**](ProtocolRule.md) | HTTP configuration. Modifiable. | [optional]
**smb** | [**ProtocolRule**](ProtocolRule.md) | SMB configuration. Modifiable. | [optional]
**fast_remove_directory_enabled** | **bool** | is fast remove directory enabled? Modifiable. | [optional] [default to False]
**provisioned** | **int** | the provisioned size of the file system in bytes. Modifiable | [optional] [default to 0]
**snapshot_directory_enabled** | **bool** | is snapshot directory enabled? Modifiable. | [optional] [default to False]
**space** | [**Space**](Space.md) | the space specification of the file system | [optional]

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


