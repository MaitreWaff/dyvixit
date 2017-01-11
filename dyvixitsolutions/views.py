from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# from django.core.context_processors import csrf
from django.views import generic

from dyvixitsolutions.models import *

from django.core import serializers

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

    rea_similaires   = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_cat_service'] = cat_service_list
    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['slider']           = rea_similaires

    return render_to_response('dyvixitsolutions/index.html', context_dict, context)

def about(request):
    """
    Page A Propos.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['slider']           = rea_similaires


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
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['list_cat_service'] = cat_service_list
    context_dict['slider']           = rea_similaires

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
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']       = astuce_list
    context_dict['list_info']         = info
    context_dict['list_cat_materiel'] = cat_materiel_list
    context_dict['slider']            = rea_similaires

    return render_to_response('dyvixitsolutions/produits.html', context_dict, context)

def references(request):
    """
    Page References des Realisations Similaires.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['slider']           = rea_similaires

    return render_to_response('dyvixitsolutions/references.html', context_dict, context)

def contact(request):
    """
    Page Contacts.
    :param request:
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['slider']           = rea_similaires


    return render_to_response('dyvixitsolutions/contacts.html', context_dict, context)

def get_service_in_cat(request, service_slug):
    """
    Page de Services par Categories.
    :param request:
    :param service_slug: Slug de la Categorie de Service.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat = CategoryService.objects.get(slug=service_slug)
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']            = astuce_list
    context_dict['list_info']              = info
    context_dict['list_services_dans_cat'] = cat.service_set.all()
    context_dict['nom_cat_service']        = cat.service_set.all()[0].titre
    context_dict['slider']                 = rea_similaires

    return render_to_response('dyvixitsolutions/services_par_cat.html', context_dict, context)

def get_materiel_in_cat(request, materiel_slug):
    """
    Page de Materiels par Categories.
    :param request:
    :param materiel_slug: Slug de la Categorie De Materiel.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat              = CategoryMateriel.objects.get(slug=materiel_slug)
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']             = astuce_list
    context_dict['list_info']               = info
    context_dict['list_materiels_dans_cat'] = cat.materiel_set.all()
    context_dict['nom_cat_materiel']        = materiel_slug
    context_dict['slider']                  = rea_similaires

    return render_to_response('dyvixitsolutions/produits_par_cat.html', context_dict, context)


def get_list_service_in_cat(request, service_slug):
    """
    Page de Services par Categories.
    :param request:
    :param service_slug: Nom de la Categorie de Service.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat = CategoryService.objects.get(slug=service_slug)
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    context_dict['list_astuce']            = astuce_list
    context_dict['list_info']              = info
    context_dict['list_services_dans_cat'] = cat.service_set.all()
    context_dict['nom_cat_service']        = cat.service_set.all()[0].libelle # service_slug
    context_dict['slider']                 = rea_similaires

    return render_to_response('dyvixitsolutions/services_par_cat.html', context_dict, context)

def get_list_materiel_in_cat(request, materiel_slug):
    """
    Page de Materiels par Categories.
    :param request:
    :param materiel_slug: Nom de la Categorie De Materiel.
    :return:
    """
    context = RequestContext(request)
    context_dict = {}

    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]
    cat              = CategoryMateriel.objects.get(slug=materiel_slug)
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]

    print materiel_slug

    context_dict['list_astuce']             = astuce_list
    context_dict['list_info']               = info
    context_dict['list_materiels_dans_cat'] = cat.materiel_set.all()
    context_dict['nom_cat_materiel']        = materiel_slug
    context_dict['slider']                  = rea_similaires

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



def update_astuce_after(request, id):
    """
    URL pour la mise a jour des Astuces dans la page.
    :param request:
    :param id:
    :return:
    """
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"

    response.write(serializers.serialize("json",
            Astuce.objects.filter(pk__gt=id)))

    return response


def update_info_after(request, id):
    """
    URL pour la mise a jour des Info dans la page.
    :param request:
    :param id:
    :return:
    """
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"

    response.write(serializers.serialize("json",
            Info.objects.filter(pk__gt=id)))

    return response




from dyvixitsolutions.form import PersonForm, ClientForm, FactureForm, LigneCommandeMaterielForm, \
    LigneCommandeServiceForm


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

        # Test Formulaire
        form      = PersonForm(post_data)
        newperson = form.save(commit=False)

        # Formulaire Client
        form_client = ClientForm(post_data)
        newclient   = form_client.save(commit=False)

        # Formulaire Facture
        form_facture = FactureForm(post_data)
        newbill      = form_facture.save(commit=False)

        # Formulaire Ligne de Commande Materiel
        form_lcmat   = LigneCommandeMaterielForm(post_data)
        newmat       = form_lcmat.save(commit=False)

        # Formulaire Ligne de Commande Service
        form_lcserv  = LigneCommandeServiceForm(post_data)
        newser       = form_lcserv.save(commit=False)

        if newperson.is_valid():
            print newperson.cleaned_data
        if newclient.is_valid():
            print newclient.cleaned_data
    else:
        context = RequestContext(request) # {}

        form    = PersonForm()
        form_client = ClientForm()
        form_facture = FactureForm()
        form_lcmat   = LigneCommandeMaterielForm()
        form_lcserv  = LigneCommandeServiceForm()

    astuce_list = Astuce.objects.order_by('-date')[:1]
    info = Info.objects.order_by('-date')[:1]

    list_cat_materiel = CategoryMateriel.objects.all()
    list_cat_service  = CategoryService.objects.all()
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:3]


    context_dict = {'form' : form, 'form_client' : form_client, 'form_facture' : form_facture, \
                    'form_lcmat' : form_lcmat, 'form_lcserv' : form_lcserv, 'list_astuce' : astuce_list, \
                    'list_info' : info, 'list_categorie_materiel' : list_cat_materiel, \
                    'list_categorie_service' : list_cat_service}
    context_dict['slider'] = rea_similaires

    return render_to_response('dyvixitsolutions/assistant.html', context_dict, context)



class ReferenceListView(generic.ListView):
    template_name = 'dyvixitsolutions/references_list.html'

    def get_queryset(self):
        return Reference.objects.all()













