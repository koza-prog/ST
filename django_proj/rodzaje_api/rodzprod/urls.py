from django.conf.urls import url
from django.urls import path
from rodzprod import views


urlpatterns = [
    url(r'^api/rodzaje/$', views.rodzaje_lista),
    url(r'^api/produkty/$', views.produkty_lista),
    url(r'^api/surowce/$', views.surowce_lista),
    url(r'^api/zaklady/$', views.zaklady_lista),
    url(r'^api/narzedzia/$', views.narzedzia_lista),
    url(r'^api/rodzaje/(?P<pk>\d+)/$', views.rodzaje_detail),
    url(r'^api/rodzaje/updatebyid/(?P<pk>\d+)$', views.rodzaje_detail),
    url(r'^api/rodzaje/deletebyid/(?P<pk>\d+)$', views.rodzaje_detail),
    path('zaklady/',views.ZakladyList.as_view())
]