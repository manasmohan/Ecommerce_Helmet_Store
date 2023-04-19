from django import urls
from django.urls import path
from django.contrib.auth import urls
from .views import SignUpView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='sign-up')



]

