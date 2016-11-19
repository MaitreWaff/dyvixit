from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# from django.core.context_processors import csrf
from dyvixitsolutions.models import *
from dyvixitsolutions.form import PersonForm

# Create your views here.
def index(request):
    context = RequestContext(request)

    service_list = CategoryService.objects.all()
    article      = Article.objects.order_by('-date')[:1]
    info         = Info.objects.order_by('-date')[:1]
    context_dict = {}
    context_dict['services_cat'] = service_list
    context_dict['article'] = article
    context_dict['info'] = info

    return render_to_response('dyvixitsolutions/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/about.html', {}, context)

def services(request):
    context = RequestContext(request)
    context_dict = {}
    article      = Article.objects.order_by('-date')[:1]
    info         = Info.objects.order_by('-date')[:1]
    context_dict['article'] = article
    context_dict['info'] = info
    cat_services = CategoryService.objects.all()
    context_dict['services_cat'] = cat_services
    return render_to_response('dyvixitsolutions/services.html', context_dict, context)

def produits(request):
    context = RequestContext(request)
    context_dict = {}
    article      = Article.objects.order_by('-date')[:1]
    info         = Info.objects.order_by('-date')[:1]
    context_dict['article'] = article
    context_dict['info'] = info
    cat_produits = CategoryProduit.objects.all()
    context_dict['produits_cat'] = cat_produits
    return render_to_response('dyvixitsolutions/produits.html', context_dict, context)

def references(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/references.html', {}, context)

def contact(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/contacts.html', {}, context)

def get_serv_in_cat(request, service_title):
    context = RequestContext(request)
    context_dict = {}
    article      = Article.objects.order_by('-date')[:1]
    info         = Info.objects.order_by('-date')[:1]
    context_dict['article'] = article
    context_dict['info'] = info
    cat = CategoryService.objects.get(titre=service_title)
    context_dict['services'] = cat.service_set.all()
    context_dict['service_cat'] = service_title
    return render_to_response('dyvixitsolutions/services_par_cat.html', context_dict, context)

def get_prod_in_cat(request, produit_title):
    context = RequestContext(request)
    context_dict = {}
    article      = Article.objects.order_by('-date')[:1]
    info         = Info.objects.order_by('-date')[:1]
    context_dict['article'] = article
    context_dict['info'] = info
    cat = CategoryProduit.objects.get(titre=produit_title)
    context_dict['produits'] = cat.produit_set.all()
    context_dict['produit_cat'] = produit_title
    return render_to_response('dyvixitsolutions/produits_par_cat.html', context_dict, context)

def test(request):
    context = RequestContext(request)
    return render_to_response('dyvixitsolutions/mycomputing.html', {}, context)


# Form processing
def process_form(request):

    if request.POST:
        context = RequestContext(request)
        form = PersonForm(request.POST.copy())
        newperson = form.save(commit=False)
    else:
        context = {}
        form = PersonForm()

    return render_to_response('dyvixitsolutions/assistant.html', {'form', form}, context)






