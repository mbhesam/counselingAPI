from django.contrib import admin
from users.models import Users


# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

