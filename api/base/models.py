from django.db import models
from django.utils.translation import ugettext_lazy as _

from .fields import StatusField


class ActiveStatusModel(models.Model):
    """
    An abstract base class model that provides active/inactive status field.

    """
    active = StatusField(_('active'), default=True)

    class Meta:
        abstract = True
