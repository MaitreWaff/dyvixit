from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# from django.core.context_processors import csrf
from dyvixitsolutions.models import *


# Create your views here.
def index(request):
    """
    Page d Acceuil.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    cat_service_list = CategoryService.objects.all()
    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    context_dict['list_cat_service'] = cat_service_list
    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info

    return render_to_response('dyvixitsolutions/index.html', context_dict, context)

def about(request):
    """
    Page A Propos.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('dyvixitsolutions/about.html', context_dict, context)

def services(request):
    """
    Page Categorie de Services.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat_service_list = CategoryService.objects.all()
    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['list_cat_service'] = cat_service_list
    return render_to_response('dyvixitsolutions/services.html', context_dict, context)

def produits(request):
    """
    Page Categories de Materiel.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list           = Astuce.objects.order_by('-date')[:1]
    info                  = Info.objects.order_by('-date')[:1]
    cat_materiel_list     = CategoryMateriel.objects.all()
    context_dict['list_astuce']       = astuce_list
    context_dict['list_info']         = info
    context_dict['list_cat_materiel'] = cat_materiel_list
    return render_to_response('dyvixitsolutions/produits.html', context_dict, context)

def references(request):
    """
    Page References des Realisations Similaires.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('dyvixitsolutions/references.html', context_dict, context)

def contact(request):
    """
    Page Contacts.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('dyvixitsolutions/contacts.html', context_dict, context)

def get_service_in_cat(request, service_title):
    """
    Page de Services par Categories.
    :param request:
    :param service_title: Nom de la Categorie de Service.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat = CategoryService.objects.get(titre=service_title)
    context_dict['list_astuce']            = astuce_list
    context_dict['list_info']              = info
    context_dict['list_services_dans_cat'] = cat.service_set.all()
    context_dict['nom_cat_service']        = service_title
    return render_to_response('dyvixitsolutions/services_par_cat.html', context_dict, context)

def get_materiel_in_cat(request, materiel_title):
    """
    Page de Materiels par Categories.
    :param request:
    :param materiel_title: Nom de la Categorie De Materiel.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat              = CategoryMateriel.objects.get(titre=materiel_title)
    print materiel_title
    context_dict['list_astuce']             = astuce_list
    context_dict['list_info']               = info
    context_dict['list_materiels_dans_cat'] = cat.materiel_set.all()
    context_dict['nom_cat_materiel']        = materiel_title
    return render_to_response('dyvixitsolutions/produits_par_cat.html', context_dict, context)


def get_list_service_in_cat(request, service_title):
    """
    Page de Services par Categories.
    :param request:
    :param service_title: Nom de la Categorie de Service.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat = CategoryService.objects.get(titre=service_title)
    context_dict['list_astuce']            = astuce_list
    context_dict['list_info']              = info
    context_dict['list_services_dans_cat'] = cat.service_set.all()
    context_dict['nom_cat_service']        = service_title
    return render_to_response('dyvixitsolutions/services_par_cat.html', context_dict, context)

def get_list_materiel_in_cat(request, materiel_title):
    """
    Page de Materiels par Categories.
    :param request:
    :param materiel_title: Nom de la Categorie De Materiel.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat              = CategoryMateriel.objects.get(titre=materiel_title)
    print materiel_title
    context_dict['list_astuce']             = astuce_list
    context_dict['list_info']               = info
    context_dict['list_materiels_dans_cat'] = cat.materiel_set.all()
    context_dict['nom_cat_materiel']        = materiel_title
    return render_to_response('dyvixitsolutions/produits_par_cat.html', context_dict, context)

def test(request):
    """
    Page de Test pour les URLs.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('dyvixitsolutions/mycomputing.html', context_dict, context)




from dyvixitsolutions.form import PersonForm, ClientForm


# Form processing
def process_form(request):
    """
    Page d Aide a la Definition des Besoins.
    :param request:
    :return:
    """


    if request.POST:
        context   = RequestContext(request)
        post_data = request.POST.copy()
        form      = PersonForm(post_data)
        newperson = form.save(commit=False)

        form_client = ClientForm(post_data)
        newclient   = form_client.save(commit=False)
        if newperson.is_valid():
            print newperson.cleaned_data
        if newclient.is_valid():
            print newclient.cleaned_data
    else:
        context = {}
        form    = PersonForm()
        form_client = ClientForm()

    context_dict = {'form' : form, 'form_client' : form_client}

    return render_to_response('dyvixitsolutions/assistant.html', context_dict, context)






