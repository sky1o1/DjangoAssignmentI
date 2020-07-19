from django.urls import path
from .views import home_view, create_view, list_view

app_name = 'blog'

urlpatterns = [
    path('home/', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list')
]