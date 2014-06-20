from django.conf.urls import patterns, include, url
from .views import InicioView, BienvenidaView

urlpatterns = patterns('',

    # url(r'^$', InicioView.as_view(), name="inicio"),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name' : 'inicio.html'}, name='loginHome'),
    url(r'^checkuser/$', BienvenidaView.as_view(), name='checkuser'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
