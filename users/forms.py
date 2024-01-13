from django import forms
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from utils import check_platform_support,is_username_exists
class SignupInformationForm(forms.Form):
    first_name = forms.CharField(label='نام', max_length=100)
    last_name = forms.CharField(label='نام خانوادگی', max_length=100)
    platform = forms.CharField(widget=forms.HiddenInput())
    username = forms.CharField(widget=forms.HiddenInput())
    gender = forms.CharField(label='جنسیت', max_length=10)
    phone_number = forms.CharField(label='شماره موبایل', max_length=11, help_text="شماره موبایل شما می بایست یازده رقمی و با 09 شروع شود")
    birthday_at = forms.DateTimeField(label='تاریخ و ساعت تولد', help_text="در صورت دانستن ساعت و تاریخ دقیق تولد خود آن را وارد نمایید در غیر اینصورت ساعت تولد را 00:00 در نظر بگیرید")
    father_name = forms.CharField(label='نام ئدر', max_length=100)
    mother_name = forms.CharField(label='نام مادر', max_length=100)
    married = forms.BooleanField(label='متاهل یا محرد', required=False)
    marriage_history = forms.IntegerField(label='تعداد سابقه ازدواج', min_value=0)
    children_numbers = forms.IntegerField(label='تعداد فرزند', min_value=0)


    def clean(self):
        cleaned_data = super().clean()
        platform = cleaned_data.get('platform')
        if check_platform_support(platform=platform) == False:
            raise Http404("platform not supported")
        username = cleaned_data.get('username')
        if is_username_exists(username=username) != True:
            raise Http404("username not exists")
        return cleaned_data
