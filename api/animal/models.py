import datetime
from django.db import models
from api.user.models import User
from model_utils.models import TimeStampedModel
from api.base.models import ActiveStatusModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Animal(TimeStampedModel, ActiveStatusModel):
    class Type:
        CAT = 1
        DOG = 2

        Choices = (
            (CAT, 'Cat'),
            (DOG, 'Dog'),
        )

    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    dob = models.DateField(_('date of birth'), default=datetime.date.today)
    type = models.IntegerField(_('type'), choices=Type.Choices, null=True, blank=True)
    user = models.ForeignKey(User, related_name='animal', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
