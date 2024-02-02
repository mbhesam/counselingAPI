from django.contrib import admin
from .models import RegisterModel

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    empty_value_display = "-خالی-"
    fields = ['phone_number','sent_sms_at','is_mobile']
