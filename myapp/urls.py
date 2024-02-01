# myapp/urls.py
from django.urls import path
from .views import home, some_view
from .views import redirect_view
urlpatterns = [
    path('', home, name='home'),
    path('some-url/', some_view, name='some-url-name'),
    path('redirect/<int:menu_item_id>/', redirect_view, name='redirect_view'),
]
