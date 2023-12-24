from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Users(models.Model):
    objects = jmodels.jManager()
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday_at = jmodels.jDateTimeField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    married = models.TextChoices("مجرد","متاهل")
    marriage_history = models.IntegerField()
    children_numbers = models.IntegerField()
    created_at = jmodels.jDateTimeField()

