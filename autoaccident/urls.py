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
    url(r'^call_log/$', views.CallLogView, name='call_log'),
    url(r'^call_list/$', views.CallList, name='call_list'),
    url(r'^client_detail/(?P<pk>[0-9]+)/$', views.ClientDetail,name='client_detail'),
    url(r'^profile/(?P<pk>[0-9]+)/edit/$', views.EditClient, name='edit_client'),
    url(r'^add_client/$', views.AddClient, name='add_client'),
    url(r'^testgraph/$', views.Analytics, name='testgraph'),
    url(r'^christmas_list/$', views.ChristmasListView, name='christmas_list'),
]
