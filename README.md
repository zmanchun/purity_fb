# purity_fb
The management APIs of FlashBlade.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: beta
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import purity_fb 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import purity_fb
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = purity_fb.AuthenticationApi()
api_token = 'api_token_example' # str | the token to log in

try:
    api_instance.login(api_token)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://purity_fb_server/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**login**](docs/AuthenticationApi.md#login) | **POST** /login | 
*AuthenticationApi* | [**logout**](docs/AuthenticationApi.md#logout) | **POST** /logout | 
*FilesystemApi* | [**create**](docs/FilesystemApi.md#create) | **POST** /1.0/filesystems | 
*FilesystemApi* | [**list**](docs/FilesystemApi.md#list) | **GET** /1.0/filesystems | 
*FilesystemApi* | [**update**](docs/FilesystemApi.md#update) | **PATCH** /1.0/filesystems | 
*FilesystemBetaApi* | [**delete**](docs/FilesystemBetaApi.md#delete) | **DELETE** /beta/filesystems | 
*SnapshotApi* | [**create**](docs/SnapshotApi.md#create) | **POST** /1.0/filesystem-snapshots | 
*SnapshotApi* | [**list**](docs/SnapshotApi.md#list) | **GET** /1.0/filesystem-snapshots | 
*SnapshotBetaApi* | [**delete**](docs/SnapshotBetaApi.md#delete) | **DELETE** /beta/filesystem-snapshots | 


## Documentation For Models

 - [ErrorResponse](docs/ErrorResponse.md)
 - [Filesystem](docs/Filesystem.md)
 - [FilesystemAttr](docs/FilesystemAttr.md)
 - [FilesystemParam](docs/FilesystemParam.md)
 - [FilesystemResponse](docs/FilesystemResponse.md)
 - [FilesystemRules](docs/FilesystemRules.md)
 - [FilesystemSpace](docs/FilesystemSpace.md)
 - [HttpRule](docs/HttpRule.md)
 - [NfsRule](docs/NfsRule.md)
 - [ObjectResponse](docs/ObjectResponse.md)
 - [PaginationInfo](docs/PaginationInfo.md)
 - [ProtocolRule](docs/ProtocolRule.md)
 - [PureError](docs/PureError.md)
 - [PureObject](docs/PureObject.md)
 - [Snapshot](docs/Snapshot.md)
 - [SnapshotResponse](docs/SnapshotResponse.md)
 - [SnapshotSpace](docs/SnapshotSpace.md)
 - [SnapshotSuffix](docs/SnapshotSuffix.md)
 - [SpaceAttr](docs/SpaceAttr.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



