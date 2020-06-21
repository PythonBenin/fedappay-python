from .mixins import AllMixin, CreateMixin, DeleteMixin, RetrieveMixin, UpdateMixin


class Resource:
    def __init__(self, base_api):
        self._base_api = base_api


class CustomerResource(AllMixin, CreateMixin, DeleteMixin, RetrieveMixin, UpdateMixin, Resource):
    _endpoint = 'customers'


class EventResource(AllMixin, RetrieveMixin, Resource):
    _endpoint = 'events'


class TransactionResource(AllMixin, CreateMixin, DeleteMixin, RetrieveMixin, Resource):
    _endpoint = 'transactions'

    def pay(self, object_id, **kwargs):
        params = kwargs.get('params', {})
        params['id'] = object_id
        kwargs['params'] = params
        return self._base_api.get(f'{self._endpoint}/pay', **kwargs)


class UserResource(AllMixin, UpdateMixin, DeleteMixin, Resource):
    _endpoint = 'accounts/users'


class AccountResource(AllMixin, CreateMixin, UpdateMixin, DeleteMixin, Resource):
    _endpoint = 'accounts'

    def current(self, object_id, **kwargs):
        return self._base_api.put(f'{self._endpoint}/current/{object_id}', data=None, **kwargs)


class SettingsResource(AllMixin, Resource):
    _endpoint = 'settings'


class AccountSettingsResource(AllMixin, CreateMixin, Resource):
    _endpoint = 'account_settings'


class RoleResource(AllMixin, Resource):
    _endpoint = 'roles'


class LogResource(AllMixin, RetrieveMixin, Resource):
    _endpoint = 'logs'


class PayoutResource(CreateMixin, RetrieveMixin, Resource):
    _endpoint = 'payouts'

    def schedule(self, data, **kwargs):
        return self._base_api.post(f'{self._endpoint}/start', data, **kwargs)
