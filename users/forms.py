from django import forms
from .models import Users
from django.utils.translation import gettext_lazy as _

class SignupInformationForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=("first_name","last_name","gender","phone_number","birthday_at","father_name","mother_name","married","marriage_history","children_numbers")
        labels = {'first_name': 'نام','last_name':'نام خانوادگی',"gender": "جنسیت",
                  'phone_number':'شماره موبایل','birthday_at':'تاریخ و ساعت تولد',
                  'father_name':'نام ئدر','mother_name':'نام مادر',
                  'married':'متاهل یا محرد','marriage_history':'تعداد سابقه ازدواج',
                  'children_numbers':'تعداد فرزند'}
        help_texts = {
            "phone_number": _("شماره موبایل شما می بایست یازده رقمی و با 09 شروع شود"),
            "birthday_at": _("در صورت دانستن ساعت و تاریخ دقیق تولد خود آن را وارد نمایید در غیر اینصورت ساعت تولد را 00:00 در نظر بگیرید")
        }
        error_messages = {
            "first_name": {
                "max_length": _("تعداد کاراکتر های نوشته شده زیاد می باشد"),
            },
            "last_name": {
                "max_length": _("تعداد کاراکتر های نوشته شده زیاد می باشد"),
            },
            "phone_number": {
                "max_length": _("فرمت شماره تلفن صحیح نمی باشد"),
            }
        }
