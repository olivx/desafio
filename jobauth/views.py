from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from jobauth.forms import SignUpForm


def logout_thanks(request):
        logout(request)
        return render(request, 'jobauth/logout.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.kind = form.cleaned_data.get('type')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'jobauth/signup.html', {'form': form})
