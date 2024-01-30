from django import forms
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from .utils import check_platform_support,is_username_exists
from jalali_date.fields import SplitJalaliDateTimeField
from jalali_date.widgets import AdminSplitJalaliDateTime

class SignupInformationForm(forms.Form):
    first_name = forms.CharField(max_length=100, label=_('نام'))
    last_name = forms.CharField(max_length=100, label=_('نام خانوادگی'))
#    platform = forms.CharField(required=False, widget=forms.HiddenInput())
#    username = forms.CharField(required=False, widget=forms.HiddenInput())
    gender = forms.ChoiceField(choices=[('مرد', _('مرد')), ('زن', _('زن'))], label=_('جنسیت'))
    phone_number = forms.CharField(max_length=11, help_text=_("شماره موبایل شما بایستی با 09 شروع شود"), label=_('شماره موبایل'))
    father_name = forms.CharField(max_length=100, label=_('نام پدر'))
    mother_name = forms.CharField(max_length=100, label=_('نام مادر'))
    married = forms.BooleanField(required=False, label=_('وضعیت تاهل؟'))
    marriage_history = forms.IntegerField(min_value=0, label=_('سابقه ازدواج'))
    children_numbers = forms.IntegerField(min_value=0, label=_('تعداد فرزند'))
    birthday_at = SplitJalaliDateTimeField(label=_('تاریخ تولد'), widget=AdminSplitJalaliDateTime)

    def clean(self):
        platform_entry = self.initial.get('platform')
        if check_platform_support(platform=platform_entry) == False:
            raise Http404("platform not supported")
        username_entry = self.initial.get('username')
        if is_username_exists(username=username_entry) != True:
            raise Http404("username not exists")
        cleaned_data = super().clean()
        cleaned_data['username'] = username_entry
        cleaned_data['platform'] = platform_entry
        return cleaned_data
