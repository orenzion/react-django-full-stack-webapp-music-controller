from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

# call this function when route = ('/','/home')


def main(request):
    return HttpResponse("Hello")  # return hello as an http response
