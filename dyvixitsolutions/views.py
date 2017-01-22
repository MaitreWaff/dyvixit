from django.shortcuts import render, render_to_response
from django.http import HttpResponse #, Http404
from django.template import RequestContext
# from django.core.context_processors import csrf
from django.views import generic

from dyvixitsolutions.models import *

from django.core import serializers

# CONSTANTES
NOMBRE_D_IMAGE_DANS_LE_SLIDER = 4

# Create your views here.
def index(request):
    """
    Page d Acceuil.
    :param request:
    :return:
    """
    # raise Http404("Waff doesn't exist!!")
    context = RequestContext(request)
    context_dict = {}

    cat_service_list = CategoryService.objects.all()
    astuce_list      = Astuce.objects.order_by('-date')[:1]
    info             = Info.objects.order_by('-date')[:1]

    rea_similaires   = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

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
    contacts         = Contact.objects.all()
    slider           = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]
    rea_similaire    = RealisationSimilaire.objects.all()

    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['slider']           = slider
    context_dict['rea_similaire']   = rea_similaire
    context_dict['list_contact']     = contacts


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
    cat_service_list = CategoryService.objects.order_by('titre') #all()
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

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
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

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
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

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
    contacts         = Contact.objects.all()
    rea_similaires   = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

    context_dict['list_astuce']      = astuce_list
    context_dict['list_info']        = info
    context_dict['slider']           = rea_similaires
    context_dict['list_contact']     = contacts


    return render_to_response('dyvixitsolutions/contacts.html', context_dict, context)

def get_service_in_cat(request, category_slug):
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
    # cat = CategoryService.objects.get(slug=service_slug)
    cat_service = CategoryService.objects.get(slug=category_slug)
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

    context_dict['list_astuce']            = astuce_list
    context_dict['list_info']              = info
    context_dict['list_services_dans_cat'] = Service.objects.filter(category = cat_service)# cat.service_set.all()
    context_dict['nom_cat_service']        = cat_service.titre # cat.service_set.all()[0].titre
    context_dict['slider']                 = rea_similaires

    return render_to_response('dyvixitsolutions/services_par_cat.html', context_dict, context)

def get_materiel_in_cat(request, category_slug):
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
    # cat              = CategoryMateriel.objects.get(slug=materiel_slug)
    cat_materiel = CategoryMateriel.objects.get(slug=category_slug)
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

    context_dict['list_astuce']             = astuce_list
    context_dict['list_info']               = info
    context_dict['list_materiels_dans_cat'] = Materiel.objects.filter(category = cat_materiel) #cat.materiel_set.all()
    context_dict['nom_cat_materiel']        = cat_materiel.titre
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
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

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
    rea_similaires = RealisationSimilaire.objects.order_by('-date')[:NOMBRE_D_IMAGE_DANS_LE_SLIDER]

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

# Differents Status dans lesquels peuvent etre une Facture...
# En Edition, Commandee, Validee, Annulee, Livree.
EDITER, COMMANDER, VALIDER, ANNULER, LIVRER = 1, 2, 3, 4, 5

# Tuple de Choix pour les Factures.
STATUS_FACTURE = (
    (EDITER, "Editer"),
    (COMMANDER, "Commander"),
    (VALIDER, "Valider"),
    (ANNULER, "Annuler"),
    (LIVRER, "Livrer"),
)


# Form processing
def process_form(request):
    """
    Page d Aide a la Definition des Besoins.
    :param request:
    :return:
    """

    context = RequestContext(request)

    if request.POST:
        # context   = RequestContext(request)
        post_data = request.POST.copy()

        # print "****** Begin POST Data"
        # print post_data
        # print "****** End POST Data"

        data_dict = dict(post_data.iterlists())
        # print data_dict

        qte_mat  = int(data_dict['nombre_postes'][0])
        qte_serv = int(data_dict['nombre_serveurs'][0])
        command_mat  = [] # Liste du Materiel commande.
        command_serv = [] # Liste des Servvices commande.
        for key in post_data:
            if "checkbox" in key:
                if post_data[key]:
                    # print "Checkbox"
        # for cb, val in data_dict.items(): # Pour toutes les paires dans le dico
        #     if "checkbox" in cb: # Si une clef est un checkbox ... C'est a dire que la ligne a ete selectionnee.
        #         if post_data[cb]: # Si le checkbox est a on
                    if ("materiel" in key) or ("service" in key): # Materiel ou Service.
                        cbstring = str(key)
                        prod_id = int(cbstring.split(" ")[2])
                        if "materiel " in key: # Materiel.
                            materiel = Materiel.objects.filter(pk=prod_id)
                            command_mat.append(materiel)
                        elif "service" in key: # Service.
                            service = Service.objects.filter(pk=prod_id)
                            command_serv.append(service)

        # print "Command Mat: ", command_mat
        # print "Command Serv: ", command_serv

        # Test Formulaire
        # form      = PersonForm(post_data)
        # newperson = form.save(commit=False)

        # Formulaire Client
        form_client = PersonForm(post_data)
        # print form_client
        # print form_client.cleaned_data

        if form_client.is_valid():
            # print "New Client Ok!"
            # print form_client.cleaned_data
            contact_info = form_client.cleaned_data
            cli_ste = contact_info['societe']
            cli_prenom = contact_info['prenom']
            cli_nom = contact_info['nom']
            cli_fonction = contact_info['fonction']
            cli_phone = contact_info['phone'] #[0]
            cli_email = contact_info['email']
            cli_address = contact_info['address']
            # print cli_address
            try:
                client, created = Client.objects.get_or_create(societe=cli_ste, prenom=cli_prenom, nom=cli_nom, fonction=cli_fonction, phone=cli_phone, email=cli_email, address=cli_address)
                #
                if created:
                    print "[*] Nouveau Client Enregistre avec Success!"
                    print client
                else:
                    print "[*] Client existant!"

                # On a une ref vers le client.
                # On crait une facture, puis les lignes de commandes relatives a cette facture.

                facture_client = Facture.objects.create(client=client)
                print "[+] Creation Facture id: ", facture_client
                print "  [*] Liste Materiels"
                for cmd in command_mat:
                    mat = Materiel.objects.get(pk=cmd[0].id)
                    nw_mat = LigneCommandeMateriel.objects.create(facture=facture_client, article=mat, quantite=qte_mat)
                    print "    [+] Nouvelle Commande Materiel: ", nw_mat

                print "  [*] Liste Services"

                for cmd in command_serv:
                    ser = Service.objects.get(pk=cmd[0].id)
                    nw_ser = LigneCommandeService.objects.create(facture=facture_client, article=ser, quantite=qte_serv)
                    print "    [+] Nouvelle Commande Service: ", nw_ser

                facture_client.status = COMMANDER
                facture_client.save()

                print "[+] Commande Facture : ", facture_client.client


                # newclient = form_client.save(commit=False)
            except Exception, e:
                print e #, type(e) #, e.args[0]


        else:
            print "Not Ok for New Client!"
            messages.error(request, "Error")


    else:

        form_client = PersonForm() #ClientForm()


    astuce_list = Astuce.objects.order_by('-date')[:1]
    info = Info.objects.order_by('-date')[:1]

    rea_similaires    = RealisationSimilaire.objects.order_by('-date')[:3]

    categories_service = CategoryService.objects.all()
    categories_materiel = CategoryMateriel.objects.all()

    list_service = Service.objects.all()
    list_materiel = Materiel.objects.all()

    context_dict = {'form_client' : form_client,  \
                     'list_astuce' : astuce_list, \
                    'list_info' : info, \
                    'list_categorie_materiel' : categories_materiel, \
                    'list_categorie_service' : categories_service}
    context_dict['slider'] = rea_similaires

    context_dict['list_service']  = list_service
    context_dict['list_materiel'] = list_materiel

    return render_to_response('dyvixitsolutions/assistant.html', context_dict, context)



class ReferenceListView(generic.ListView):
    template_name = 'dyvixitsolutions/references_list.html'


    def get_queryset(self):
        return Reference.objects.all()













