from django.conf.urls import patterns, include, url
from dyvixitsolutions import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dyvixproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^produits/$', views.produits, name='produits'),
    url(r'^references/$', views.references, name='references'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^test/$', views.test, name='test'),
    url(r'^move/$', views.move, name='move'),
)
