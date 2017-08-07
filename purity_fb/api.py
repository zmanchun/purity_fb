from purity_fb.apis.authentication_api import AuthenticationApi
from purity_fb.apis.file_system_api import FileSystemApi
from purity_fb.apis.file_system_beta_api import FileSystemBetaApi
from purity_fb.apis.file_system_snapshot_api import FileSystemSnapshotApi
from purity_fb.apis.file_system_snapshot_beta_api import FileSystemSnapshotBetaApi
from purity_fb.api_client import ApiClient
from purity_fb import rest

import urllib3


class PurityFb:
    DEFAULT_READ_TIMEOUT = 30.0
    DEFAULT_CONN_TIMEOUT = 10.0
    DEFAULT_RETRIES = 5

    def __init__(self, host, api_token=None):
        self._api_client = ApiClient(host="https://{}/api".format(host))
        self.request_timeout = urllib3.Timeout(
            connect=PurityFb.DEFAULT_CONN_TIMEOUT,
            read=PurityFb.DEFAULT_READ_TIMEOUT)
        self.retries = urllib3.Retry(total=PurityFb.DEFAULT_RETRIES)
        self._auth = AuthenticationApi(api_client=self._api_client)
        self._file_system = FileSystemApi(api_client=self._api_client)
        self._file_system_beta = FileSystemBetaApi(api_client=self._api_client)
        self._file_system_snapshot = FileSystemSnapshotApi(api_client=self._api_client)
        self._file_system_snapshot_beta = FileSystemSnapshotBetaApi(api_client=self._api_client)
        if api_token:
            self.login(api_token)

    def login(self, api_token):
        try:
            self.logout()
        except rest.ApiException:
            pass
        res = self._auth.login_with_http_info(api_token=api_token)
        self._api_client.default_headers['x-auth-token'] = res[2]['x-auth-token']
        return res[1]

    def logout(self):
        return self._auth.logout_with_http_info()[1]

    @property
    def request_timeout(self):
        return self._api_client.rest_client.pool_manager.connection_pool_kw['timeout']

    @request_timeout.setter
    def request_timeout(self, value):
        self._api_client.rest_client.pool_manager.connection_pool_kw['timeout'] = value

    @property
    def request_retry(self):
        return self._api_client.rest_client.pool_manager.connection_pool_kw['retries']

    @request_retry.setter
    def request_retry(self, value):
        self._api_client.rest_client.pool_manager.connection_pool_kw['retries'] = value

    @property
    def authentication(self):
        return self._auth

    @property
    def file_system(self):
        return self._file_system

    @property
    def file_system_snapshot(self):
        return self._file_system_snapshot

    @property
    def file_system_beta(self):
        return self._file_system_beta

    @property
    def file_system_snapshot_beta(self):
        return self._file_system_snapshot_beta
