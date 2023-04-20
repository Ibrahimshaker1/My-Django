from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


def relative(request):

    return render(request, "frist_app/relative_url.html",)

@login_required
def special(request):
    return HttpResponse("hellllo")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/other")

def register(request):

    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save()
            profile.user = user
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    my_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'frist_app/index.html', context=my_dict)


def other(request):
    return render(request, "frist_app/other.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/other')

            else:
                return HttpResponse("Account not active")
        else:
            print("someone")
            print(f"username:{username} and password{password}")
            return HttpResponse("invalid")
    else:
        return render(request, "frist_app/login.html", {})
