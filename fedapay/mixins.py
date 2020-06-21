class AllMixin:
    def all(self, **kwargs):
        return self._base_api.get(self._endpoint, **kwargs)


class CreateMixin:
    def create(self, data, **kwargs):
        return self._base_api.post(self._endpoint, data, **kwargs)


class RetrieveMixin:
    def retrieve(self, object_id, **kwargs):
        return self._base_api.get(f'{self._endpoint}/{object_id}', **kwargs)


class DeleteMixin:
    def delete(self, object_id, **kwargs):
        return self._base_api.delete(f'{self._endpoint}/{object_id}', **kwargs)


class UpdateMixin:
    def update(self, object_id, data, **kwargs):
        return self._base_api.put(f'{self._endpoint}/{object_id}', data, **kwargs)
