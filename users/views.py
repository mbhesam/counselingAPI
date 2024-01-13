from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import SignupInformationForm
from .models import Users


def get_signup_info(request,platform,username):
    if request.method == "POST":
        form = SignupInformationForm(request.POST,initial={'platform': platform, 'username': username})
        if form.is_valid():
            user_data = form.cleaned_data
            user = Users(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                platform=user_data['platform'],
                username= user_data['username'],
                gender=user_data['gender'],
                phone_number=user_data['phone_number'],
                birthday_at=user_data['birthday_at'],
                father_name=user_data['father_name'],
                mother_name=user_data['mother_name'],
                married=user_data['married'],
                marriage_history=user_data['marriage_history'],
                children_numbers=user_data['children_numbers']
            )
            user.save()
            return HttpResponseRedirect("/users/thanks/")
    else:
        form = SignupInformationForm()
    return render(request, "form.html", {"form": form})