from purity_fb.apis.authentication_api import AuthenticationApi
from purity_fb.apis.filesystem_api import FilesystemApi
from purity_fb.apis.filesystem_beta_api import FilesystemBetaApi
from purity_fb.apis.snapshot_api import SnapshotApi
from purity_fb.apis.snapshot_beta_api import SnapshotBetaApi
from purity_fb.api_client import ApiClient


class PurityFb:
    def __init__(self, host, api_token=None):
        self._api_client = ApiClient(host="{}/api".format(host))
        self._auth_api = AuthenticationApi(api_client=self._api_client)
        self._filesystem_api = FilesystemApi(api_client=self._api_client)
        self._filesystem_beta_api = FilesystemBetaApi(api_client=self._api_client)
        self._snapshot_api = SnapshotApi(api_client=self._api_client)
        self._snapshot_beta_api = SnapshotBetaApi(api_client=self._api_client)
        if api_token:
            self.login(api_token)

    def login(self, api_token):
        res = self._auth_api.login_with_http_info(api_token=api_token)
        self._api_client.default_headers['x-auth-token'] = res[2]['x-auth-token']
        return res[1]

    def logout(self):
        return self._auth_api.logout_with_http_info()[1]

    def filesystem_api(self):
        return self._filesystem_api

    def snapshot_api(self):
        return self._snapshot_api

    def filesystem_beta_api(self):
        return self._filesystem_beta_api

    def snapshot_beta_api(self):
        return self._snapshot_beta_api
