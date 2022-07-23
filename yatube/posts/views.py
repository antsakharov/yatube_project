from importlib.resources import path
from django.forms import SlugField
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Главная страница
def index(request):    
    return HttpResponse('Главная страница')
def group_posts(request,slug):
    return HttpResponse(f'Посты отфильтрованные по группам {slug}')