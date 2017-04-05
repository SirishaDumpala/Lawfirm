from django.conf.urls import url
from django.conf.urls import include

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clients/$', views.ClientListView, name='clients'),
    url(r'^clients/(?P<pk>\d+)$', views.ClientDetailView.as_view(), name='client_detail'),
    url(r'^new_client_signup/$', views.NewClient, name='new_client_signup'),
    url(r'^otherparty_info/$', views.OtherParty, name='otherparty_info'),
    url(r'^accident_details/$', views.AccidentDetails, name='accident_details'),
    url(r'^appointment_details/$', views.AppointmentDetails, name='appointment_details'),
    url(r'^appointment_list/$', views.AppointmentList, name='appointment_list'),
]
