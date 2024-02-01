from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
def home(request):
    menu_items = MenuItem.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'home.html', context)

def ChangeAddView(request):
    return render(request, 'change_add_view_template.html')
def some_view(request):
    # Your view logic here
    return render(request, 'some_template.html')
def redirect_view(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    return redirect(menu_item.url)