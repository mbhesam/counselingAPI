from django.contrib import admin
from .models import Category, SubCategory, Advices


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = "-خالی-"
    fields = ["name"]
    list_display = ["عنوان"]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    empty_value_display = "-خالی-"
    fields = ["category", "name"]
    list_display = ["عنوان", "اسم زیر عنوان"]

@admin.register(Advices)
class AdvicesAdmin(admin.ModelAdmin):
    empty_value_display = "-خالی-"
    fields = ["category", "subcategory", "content"]
    list_display = ["عنوان اصلی", "زیر عنوان", "محتوا"]


