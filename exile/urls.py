from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^page/(?P<alias>\w+)/$', views.page, name="page"),
    url(r'^contacto/', views.ContactoSupra.as_view(), name="contacto" )
]
