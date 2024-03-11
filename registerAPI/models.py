from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class RegisterModel(models.Model):
    objects = jmodels.jManager()
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, verbose_name='شماره همراه')
    sent_sms_at = jmodels.jDateTimeField(verbose_name='زمان فرستاده شدن پیامک')
    is_mobile = models.BooleanField(verbose_name='آیا این شماره موبایل است؟')
    class Meta:
        verbose_name = 'ثبت نام'
        verbose_name_plural = 'ثبت نام ها'
