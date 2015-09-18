from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from dyvixitsolutions.models import *

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/index.html', {}, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/index.html', {}, context)

def services(request):
    context = RequestContext(request)
    context_dict = {}
    cat_services = CategoryService.objects.all()
    context_dict['cat_services'] = cat_services
    return render_to_response('dyvixitsolutions/services.html', context_dict, context)

def produits(request):
    context = RequestContext(request)
    context_dict = {}
    cat_produits = CategoryProduit.objects.all()
    context_dict['cat_produits'] = cat_produits
    return render_to_response('dyvixitsolutions/produits.html', context_dict, context)

def references(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/index.html', {}, context)

def contact(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/index.html', {}, context)

def move(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/move.html', {}, context)

def test(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/mycomputing.html', {}, context)
