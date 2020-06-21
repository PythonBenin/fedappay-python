from requests import request

from . import resources


class FedaPayAPI:
    _version = '1'

    def __init__(self, public_key, private_key, sandbox=False, version='1', verify_ssl=True, timeout=5):
        self._sandbox = sandbox
        self._public_key = public_key
        self._private_key = private_key
        self._verify_ssl = verify_ssl
        self._version = f'v{version}'
        self._timeout = timeout
        self._token = None

        self.User = resources.UserResource(self)  # todo doesn't work with private_key like auth
        self.Transaction = resources.TransactionResource(self)
        self.Event = resources.EventResource(self)
        self.Customer = resources.CustomerResource(self)
        self.Account = resources.AccountResource(self)  # todo doesn't work with private_key like auth
        self.AccountSettings = resources.AccountSettingsResource(self)  # todo doesn't work with private_key like auth
        self.Settings = resources.SettingsResource(self)  # todo doesn't work with private_key like auth
        self.Role = resources.RoleResource(self)  # todo doesn't work with private_key like auth
        self.Log = resources.LogResource(self)
        self.Payout = resources.PayoutResource(self)  # doesn't work need custom authorization from Nautilus

    def _get_url(self, endpoint):
        url = f"https://api.fedapay.com"
        if self._sandbox:
            url = "https://sandbox-api.fedapay.com"

        if endpoint.startswith('/'):
            endpoint = endpoint[1:]

        return f'{url}/{self._version}/{endpoint}'

    def _get_headers(self):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._private_key}"
        }

        return headers

    def _request(self, method, endpoint, data, params=None, **kwargs):
        """ Do requests """
        if params is None:
            params = {}
        url = self._get_url(endpoint)
        auth = None

        return request(
            method=method,
            url=url,
            verify=self._verify_ssl,
            auth=auth,
            params=params,
            data=data,
            timeout=self._timeout,
            headers=self._get_headers(),
            **kwargs
        )

    def get(self, endpoint, **kwargs):
        """ Get requests """
        return self._request("GET", endpoint, None, **kwargs)

    def post(self, endpoint, data, **kwargs):
        """ POST requests """
        return self._request("POST", endpoint, data, **kwargs)

    def put(self, endpoint, data, **kwargs):
        """ PUT requests """
        return self._request("PUT", endpoint, data, **kwargs)

    def delete(self, endpoint, **kwargs):
        """ DELETE requests """
        return self._request("DELETE", endpoint, None, **kwargs)

    def options(self, endpoint, **kwargs):
        """ OPTIONS requests """
        return self._request("OPTIONS", endpoint, None, **kwargs)
