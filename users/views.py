from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import SignupInformationForm


def get_signup_info(request):
    if request.method == "POST":
        form = SignupInformationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/users/thanks/")
    else:
        form = SignupInformationForm()
    return render(request, "form.html", {"form": form})