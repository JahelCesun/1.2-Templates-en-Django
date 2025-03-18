from django.urls import path
from templateapp.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
]