from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='empty'),
    path('home/<int:id>/', Home.as_view(), name='home'),
    path('info', Info.as_view(), name='info'),
]