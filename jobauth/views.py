from django.shortcuts import render

# Create your views here.

def logout_thanks(request):
    return render(request, 'core/logout.html')
