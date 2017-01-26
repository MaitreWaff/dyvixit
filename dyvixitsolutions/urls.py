from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from dyvixitsolutions import views

import django.views.defaults

from dyvixitsolutions.models import Materiel, Service, Facture

# handler404 = 'path.to.views.custom404'

from django.views.generic import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dyvixproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^assistant-cahier-des-charges-informatique/$', views.cahierDesCharges, name='cahier_des_charges_informatique'),
    url(r'^assistant/$', views.process_form, name='cahier_des_charges_informatique'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^produits/$', views.produits, name='produits'),
    url(r'^produits/(?P<category_slug>[-\w]+)/$', views.get_materiel_in_cat, name='get_materiel_in_cat'),
    url(r'^references/$', views.ReferenceListView.as_view(), name='references'),
    url(r'^services/$', views.services, name='services'),
    url(r'^services/(?P<category_slug>[-\w]+)/$', views.get_service_in_cat, name='get_service_in_cat'),
    url(r'^services/(?P<service_slug>[-\w]+)/$', views.ServiceDetailView.as_view(), name='details_service'), # (?P<category_slug>[-\w]+)/

    url(r'^update-astuce-after/(?P<id>\d+)/$', views.update_astuce_after,),
    url(r'^update-info-after/(?P<id>\d+)/$', views.update_info_after,),


    # url(r'^move/$', views.move, name='move'),
    # url(r'^produit/category/(?P<materiel_slug>[-\w]+)/$', views.get_list_materiel_in_cat, name='details_materiel'),
    # url(r'^service/category/(?P<service_slug>[\-w]+)/$', views.get_list_service_in_cat, name='details_service'),

    # url(r'^test/(?P<produit_slug>\w+)/$', views.get_list_service_in_cat,
    #     kwargs = {
    #         'queryset' : Service.objects.all(),
    #     },
    #     name = 'liste_service'),
    #
    # url(r'^test/(?P<produit_slug>\w+)/$', views.get_list_materiel_in_cat,
    #     kwargs= {
    #         'queryset' : Materiel.objects.all(),
    #     },
    #     name='liste_materiel'),
    # url(r'^404/$', django.views.defaults.page_not_found,),



    # url(r'^waffo/$', 'django.views.generic',
    #     kwargs={
    #         'template' : 'index.html',
    #         'extra_context' : {'item_list' : lambda : Facture.objects.all()}
    #     },
    #     name='waffo'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
