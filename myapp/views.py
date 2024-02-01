from django.shortcuts import render
from .models import MenuItem

def home(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'home.html', context)
