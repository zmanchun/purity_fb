# purity_fb.AuthenticationApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /login | 
[**logout**](AuthenticationApi.md#logout) | **POST** /logout | 


# **login**
> login(api_token)



log in the server

### Example 
```python
from __future__ import print_statement
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| the token to log in | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()



log out from the server

### Example 
```python
from __future__ import print_statement
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = purity_fb.AuthenticationApi()

try: 
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

