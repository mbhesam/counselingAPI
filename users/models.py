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
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    gender = models.CharField(max_length=5,choices=GENDER_CHOICES,null=False)
    birthday_at = jmodels.jDateTimeField(null=False)
    father_name = models.CharField(max_length=100,null=False)
    mother_name = models.CharField(max_length=100,null=False)
    phone_number = models.CharField(max_length=11,null=False)
    married = models.CharField(max_length=8,choices=MARRIED,null=False)
    marriage_history = models.IntegerField(null=False)
    children_numbers = models.IntegerField(null=False)
    created_at = jmodels.jDateTimeField(null=False)

