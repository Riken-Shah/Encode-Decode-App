from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home_page'),
    path('encode',views.encode, name='Encode'),
    path('what_is_it',views.whats_it, name='whats_it'),
    path('decode',views.decode, name='Decode'),
]