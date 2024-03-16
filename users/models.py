from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Users(models.Model):
    GENDER_CHOICES = (
        ('مرد', 'مرد'),
        ('زن', 'زن'),
    )
    MARRIED=(
        ("مجرد", "مجرد"),
        ("متاهل", "متاهل"),
    )
    objects = jmodels.jManager()
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, verbose_name='نام')
    last_name = models.CharField(max_length=100, null=False, verbose_name='نام خانوادگی')
    platform = models.CharField(max_length=20, null=False, verbose_name='پلتفرم پاسخ گویی ربات')
    username = models.CharField(max_length=200, null=False, unique=True, verbose_name='آی دی')
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES, null=False, verbose_name='جنسیت')
    birthday_at = jmodels.jDateTimeField(null=False, verbose_name='تاریخ تولد')
    father_name = models.CharField(max_length=100, null=False, verbose_name='نام پدر')
    mother_name = models.CharField(max_length=100, null=False, verbose_name='نام مادر')
    phone_number = models.CharField(max_length=11, null=False, verbose_name='شماره تلفن همراه')
    married = models.CharField(max_length=8, choices=MARRIED, null=False, verbose_name='متاهل')
    marriage_history = models.IntegerField(null=False, verbose_name='سابقه تاهل')
    children_numbers = models.IntegerField(null=False, verbose_name='تعداد فرزندان')
    created_at = jmodels.jDateTimeField(auto_now_add=True, null=False, verbose_name='ساخته شده در زمان')

    class Meta:
        verbose_name = 'مراجعه کنندگان'
        verbose_name_plural = 'مراجعه کنندگان'

    def __str__(self):
        return self.last_name
