from django.urls import path
from .views import (
    home,
    menu_category,
    menu,
    booktable,
    contact,
    event)


urlpatterns = [
    path('', home, name='home'),
    path('menu', menu, name = 'menu'),
    path('menu/category/<int:id>', menu_category, name = 'menu_id'),
    path('booktable', booktable, name='booktable'),
    path('event', event, name = 'Event'),
    path('contact', contact, name = 'contact')
]
