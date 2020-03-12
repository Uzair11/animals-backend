from django.db import models


class StatusField(models.BooleanField):
    """
    A StatusField that maintains the status of a model.

    By default, default=True.

    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', True)
        super(StatusField, self).__init__(*args, **kwargs)
