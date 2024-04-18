from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home_page(request):
    user = request.user
    client_ip = request.META.get('REMOTE_ADDR')

    context = {
        "user": user,
        "ip_local": client_ip,
    }

    return render(request, 'home.html', context=context)
