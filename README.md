# purity_fb
Client for FlashBlade REST API 1.0, developed by Pure Storage, Inc. (http://www.purestorage.com/).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://www.purestorage.com](http://www.purestorage.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/zmanchun/purity_fb.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/zmanchun/purity_fb.git`)

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
from purity_fb import PurityFb, FileSystem, SnapshotSuffix, rest

# create PurityFb object for a certain array
fb = PurityFb("10.255.8.20")
try:
    fb.login("T-e7e551be-fe5d-4669-baf5-670cd8ea0560")
    fs_obj = FileSystem(name="myfs", provisioned=50000)
    fb.file_system.create(fs_obj)
    fb.file_system.list()
    fb.file_system_snapshot.create(sources=["myfs"], suffix=SnapshotSuffix("mysnap"))
    fb.file_system_snapshot.list()
    fb.logout()
except rest.ApiException as e:
    print("Exception: %s\n" % e)
```

## Documentation for PurityFb

A *PurityFb* object represents an FlashBlade device.

```class purity_fb.PurityFb(host, api_token=None)```

The argument *host* is required, which is the IP address or host name of the device, 
while *api_token* is optional, which if present, will be used to log in to the device.


### Methods


Two methods are provided for logging into and out from a device.

Method | Parameters | Description
------------- | ------------- | -------------
*login* | *api_token* | Login to the REST server with a specified *api-token*. **This method must be executed successfully before making any function calls to any APIs.** | 
*logout* | n/a | Logout from the REST server |


### **Endpoint Properties**


Once *login* succeeds, different endpoints could be accessed through the following read-only properties of *PurityFb* objects.

Property | Type | Descripstion
------------ | ------------- | -------------
*file_system* | [**FileSystemApi**](docs/FileSystemApi.md) | API for the file system endpoint (**create**, **list**, and **update**) |
*file_system_beta* | [**FileSystemBetaApi**](docs/FileSystemBetaApi.md) | API for the beta file system endpoint  (**delete** only) |
*file_system_snapshot* | [**FileSystemSnapshotApi**](docs/FileSystemSnapshotApi.md) | API for the file system snapshots endpoint (**create** and **list**) |
*file_system_snapshot_beta* | [**FileSystemSnapshotBetaApi**](docs/FileSystemSnapshotBetaApi.md) | API for the beta file system snapshots endpoint (**delete** only) |


#### Call with HTTP information
Every method of each endpoint returns an object representing the body of the response from the server.
If other information such as response status code or response header is needed, the corresponding method 
```XXX_with_http_info()``` can be used. 
  
For example,

```python
fb = purity_fb.PurityFb("10.255.3.20")
fb.login("T-1eeb15b4-1288-49b2-b0cc-5a7c9e5d524f")
data = fb.file_system.create(FileSystem(name="myfs"))
```

Here *response_data* has type [FileSystemResponse](docs/FileSystemResponse.md). 
And if call with HTTP information, both the response status and header will be returned as well.

```(data, status, header) = fb.file_system.create_with_http_info(FileSystem(name="myfs"))```

### Request Timeout Configuration


#### Global Request Timeout

The property *PurityFb.request_timeout* allows one to get or update the global request timeout used by default for
all API calls. The default *request_timeout* is 10 seconds for connection, and 30 seconds for read.


Property | Type | Descripstion
------------ | ------------- | -------------
*request_timeout* | [**urllib3.Timeout**](http://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html) | Set or get the global request timeout for accessing the device. |


For example, ```fb.request_timeout = urllib3.Timeout(connect=8.0, read=20.0)```. This updates all API call to have 8 seconds connection
timeout and 20 seconds read timeout by default.


#### One-time-only Request Timeout


All APIs support the keyword parameter *_request_timeout* 
(of type [**urllib3.Timeout**](http://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html) ) 
to specify request timeout for a specific API call.

For example, 

```fb.file_system.create(FileSystem(name="myfs"), _request_timeout=urllib3.Timeout(connect=5.0, read=15.0))}} ```


### Retries

The property *PurityFb.request_retry* allows one to get or update the global retry setting used by default for
all API calls. The default *request_retry* is 5 retries per call.


Property | Type | Descripstion
------------ | ------------- | -------------
*request_retry* | [**urllib3.Retry**](http://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html) | Set or get the global request timeout for accessing the device. |


For example, ```fb.request_retry = urllib3.Retry(total=20, connect=15, read=15)```. This updates all API call to have 
at most 20 retries in total, among which at most 15 connection retries and at most 15 read retries.


## Documentation For Models

 - [FileSystem](docs/FileSystem.md)
 - [FileSystemResponse](docs/FileSystemResponse.md)
 - [FileSystemRules](docs/FileSystemRules.md)
 - [FileSystemSnapshot](docs/FileSystemSnapshot.md)
 - [FileSystemSnapshotResponse](docs/FileSystemSnapshotResponse.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [NfsRule](docs/NfsRule.md)
 - [ObjectResponse](docs/ObjectResponse.md)
 - [PaginationInfo](docs/PaginationInfo.md)
 - [ProtocolRule](docs/ProtocolRule.md)
 - [PureObject](docs/PureObject.md)
 - [SnapshotSuffix](docs/SnapshotSuffix.md)
 - [Space](docs/Space.md)


## Documentation For Authorization


## ApiTokenQueryParam

- **Type**: API key
- **API key parameter name**: api-token
- **Location**: URL query string

## AuthTokenHeader

- **Type**: API key
- **API key parameter name**: x-auth-token
- **Location**: HTTP header


## Author

info@purestorage.com

