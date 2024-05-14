from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from .views import *

class CustomMiddleware(MiddlewareMixin):

 def process_request(self, request):
    if not request.user.is_authenticated:
        if request.path not in ['/loginpage', '/register']:
            return redirect('loginpage')
