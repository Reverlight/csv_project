from django.contrib import admin
from django.urls import path

from .views import login_user, scheme_list, scheme_add, data_set_list, get_download_status, delete_scheme

urlpatterns = [
    path('login/', login_user, name='login'),
    path('scheme_add/', scheme_add, name='scheme_add'),
    path('data_set/', data_set_list, name='data_set'),
    path('get_download_status/', get_download_status, name='get_download_status'),
    path('delete/<int:pk>/', delete_scheme, name='delete_scheme'),
    path('', scheme_list, name='scheme_list'),
]
