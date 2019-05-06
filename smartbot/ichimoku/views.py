from django.shortcuts import render

# Create your views here.


from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User_credentials
# Create your views here.
import requests
from django.http import HttpResponseRedirect, HttpResponse

def test(request):
    return HttpResponse('It works')