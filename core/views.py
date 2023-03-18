from django.shortcuts import render, redirect
# import login_required
from django.contrib.auth.decorators import login_required
from accounts.models import Profile


# Create your views here.


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    return redirect('/accounts/login')


@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    return render(request, 'dashboard/edit-profile.html', context={'profile': profile})


@login_required
def my_account(request):
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    return render(request, "dashboard/profile.html", context={'profile': profile})
