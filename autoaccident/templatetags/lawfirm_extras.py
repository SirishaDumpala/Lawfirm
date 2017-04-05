from django import template
from ..models import Client, Appointment

register = template.Library()

@register.inclusion_tag('lawfirm/client_list.html')
def get_client_list():
    return {'client_list': Clients.objects.all()}

def get_appointment_list():
    return {'appointment_list': Appointment.objects.all()}
