from requests import request

from fedapay.resources import UserResource, TransactionResource, CustomerResource, AccountResource, SettingsResource, RoleResource, LogResource


class BaseAPI:
    version = '1'

    def __init__(self, public_key, private_key, sandbox=False, version='1', verify_ssl=True, timeout=5):
        self.sandbox = sandbox
        self.public_key = public_key
        self.private_key = private_key
        self.verify_ssl = verify_ssl
        self.version = f'v{version}'
        self.timeout = timeout

    def _get_url(self, endpoint):
        url = f"https://api.fedapay.com"
        if self.sandbox:
            url = "https://sandbox-api.fedapay.com"

        if endpoint.startswith('/'):
            endpoint = endpoint[1:]

        return f'{url}/{self.version}/{endpoint}'

    def _get_headers(self):
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.private_key}"
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
            verify=self.verify_ssl,
            auth=auth,
            params=params,
            data=data,
            timeout=self.timeout,
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


class FedaPayAPI(BaseAPI):
    def __init__(self, public_key, private_key, sandbox=False, version='1', verify_ssl=True, timeout=5):
        super().__init__(public_key, private_key, sandbox, version, verify_ssl, timeout)
        self.User = UserResource(self)
        self.Transaction = TransactionResource(self)
        self.Customer = CustomerResource(self)
        self.Account = AccountResource(self)
        self.Settings = SettingsResource(self)
        self.Role = RoleResource(self)
        self.Log = LogResource(self)
