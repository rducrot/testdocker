from django.shortcuts import render
from django.conf import settings
# Create your views here.

def home(request):

    context = {
        'app_display': settings.APP_DISPLAY_NAME,
    }

    return render(request, 'home/index.html', context=context)
