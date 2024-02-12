from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    return HttpResponse("Rango says hey there partner! <br><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <br><a href='/rango/'>Index</a>")


def index(request):
   
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context = {'boldmessage': 'This is the about page.', 
               }
    return render(request, 'rango/about.html', context)

def show_category(request, category_name_slug):
    context_dict = {}
    
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)
