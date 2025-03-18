from django.urls import path
from .views import store, main,about_me

urlpatterns = [
    path('', main, name='main'),
    path('store',store,name='store'),
    path('about_me', about_me,name='about_me'),
]