from django.forms import ModelForm
from django import forms
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking Statute of limitation date range.
from .models import Client, ClientAddress, ClientVehicle, OtherPartyInformation, AccidentDetails, Appointment, CallLog

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class NewClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ['first_name', 'middle_name', 'last_name',
                    'client_type', 'phone_number', 'date_of_birth','gender', 'driver_license', 'date_of_accident',]
        #labels = {'statute_date': _('filing_date'),}
        #help_texts = {'statute_date': _('Enter the date 2 years from the date of accident.'),}

class ClientAddressForm(ModelForm):
    class Meta:
        model = ClientAddress
        fields = ['address_1', 'address_2', 'city', 'state', 'zip_code',]

class ClientVehicleForm(ModelForm):
    class Meta:
        model = ClientVehicle
        widgets = {'carseat': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ['vehicle_year', 'vehicle_make', 'vehicle_model', 'vehicle_color', 'vehicle_registration', 'damage_location', 'damage_description',
        'carseat',]

class OtherPartyInfoForm(ModelForm):
    class Meta:
        model = OtherPartyInformation
        fields = ['client', 'otherparty_driver_name', 'otherparty_phonenumber', 'otherparty_gender', 'otherparty_date_of_birth',
        'otherparty_driver_license', 'otherparty_number_of_passengers', ]

class OtherPartyAddressForm(ModelForm):
    class Meta:
        model = OtherPartyInformation
        fields = ['otherparty_address_1', 'otherparty_address_2', 'otherparty_city', 'otherparty_state',
        'otherparty_zip_code',]

class OtherPartyVehicleForm(ModelForm):
    class Meta:
        model = OtherPartyInformation
        #widgets = {'carseat': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ['otherparty_vehicle_year', 'otherparty_vehicle_make', 'otherparty_vehicle_model', 'otherparty_vehicle_color',
        'otherparty_vehicle_registration', 'otherparty_damage_location', 'otherparty_damage_description',]

class AccidentDetailsForm(ModelForm):
    class Meta:
        model = AccidentDetails
        widgets = {'police_report': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ['client', 'date_of_accident', 'time_of_accident', 'weather_condition', 'city_of_accident', 'intersection_of_accident', 'police_report', 'police_report_number', 'accident_description',]

class AppointmentForm(forms.ModelForm):

    #appointment_date = forms.DateTimeField(widget = DateTimeWidget(usel10n = True, bootstrap_version = 3))
    class Meta:
        model = Appointment

        widgets = {'existing_client': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                   'appointment_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                  'appointment_time': TimeWidget(attrs= {'id':"yourtimeid"}, usel10n = True, bootstrap_version=3)}
        fields = ('existing_client','caller_first_name', 'caller_last_name', 'type_of_appointment', 'further_appointment_notes', 'phone_number','appointment_date','appointment_time',)

class CallLogForm(forms.ModelForm):
    class Meta:
        model = CallLog

        call_date = DateField(widget = AdminDateWidget)
        fields = ('client', 'caller_name', 'caller_number', 'call_notes')
