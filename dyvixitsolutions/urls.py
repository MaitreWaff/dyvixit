from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from dyvixitsolutions import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dyvixproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^assistant-cahier-des-charges-informatique/$', views.cahierDesCharges, name='cahier_des_charges_informatique'),
    url(r'^assistant/$', views.process_form, name='cahier_des_charges_informatique'),
    url(r'^services/$', views.services, name='services'),
    url(r'^services/category/(?P<service_title>\w+)/$', views.get_service_in_cat, name='get_service_in_cat'),
    url(r'^produits/$', views.produits, name='produits'),
    url(r'^produits/category/(?P<produit_title>\w+)/$', views.get_materiel_in_cat, name='get_materiel_in_cat'),
    url(r'^references/$', views.references, name='references'),
    url(r'^contact/$', views.contact, name='contact'),

    # url(r'^move/$', views.move, name='move'),
    url(r'^service/category/(?P<service_title>\w+)/$', views.get_service_in_cat, name='details_service'),
    url(r'^produit/category/(?P<produit_title>\w+)/$', views.get_materiel_in_cat, name='details_materiel'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
