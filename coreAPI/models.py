from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ManyToManyField("Category", related_name="subcategory")
    name = models.CharField(max_length=255)

class Advices(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ManyToManyField("Category", related_name="advices")
    subcategory = models.ManyToManyField("SubCategory", related_name="advices", blank=True)
    content = models.TextField()


