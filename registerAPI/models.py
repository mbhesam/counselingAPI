from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class RegisterModel(models.Model):
    objects = jmodels.jManager()
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11)
    sent_sms_at = jmodels.jDateTimeField()
    is_mobile = models.BooleanField()
