from django.forms import ModelForm
from django import forms
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking Statute of limitation date range.
from .models import Client, ClientAddress, ClientVehicle, OtherPartyInformation, AccidentDetails, Appointment, CallLog, DoctorInfo, ClaimInfo, InsuranceInformation

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class NewClientForm(ModelForm):

    class Meta:
        model = Client
        widgets = {'date_of_accident': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                    'medicare_coverage': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'medicaid_coverage': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    }
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number', 'date_of_birth','gender', 'driver_license','ssnumber', 'medicare_coverage', 'medicaid_coverage', 'date_of_accident','client_type', 'injuries',]
        #labels = {'statute_date': _('filing_date'),}
        #help_texts = {'statute_date': _('Enter the date 2 years from the date of accident.'),}

class ClientAddressForm(ModelForm):
    class Meta:
        model = ClientAddress
        fields = ['client', 'address_1', 'address_2', 'city', 'state', 'zip_code',]

class ClientVehicleForm(ModelForm):
    class Meta:
        model = ClientVehicle
        widgets = {'carseat': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ['client', 'vehicle_year', 'vehicle_make', 'vehicle_model', 'vehicle_color', 'vehicle_registration', 'damage_description',
        'carseat',]

class OtherPartyInfoForm(ModelForm):
    class Meta:
        model = OtherPartyInformation
        fields = ['client', 'otherparty_driver_name', 'otherparty_phonenumber', 'otherparty_gender', 'otherparty_date_of_birth',
        'otherparty_driver_license', ]

class OtherPartyAddressForm(ModelForm):
    class Meta:
        model = OtherPartyInformation
        fields = ['client', 'otherparty_address_1', 'otherparty_address_2', 'otherparty_city', 'otherparty_state',
        'otherparty_zip_code',]

class OtherPartyVehicleForm(ModelForm):
    class Meta:
        model = OtherPartyInformation
        #widgets = {'carseat': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}
        fields = ['client', 'otherparty_vehicle_year', 'otherparty_vehicle_make', 'otherparty_vehicle_model', 'otherparty_vehicle_color',
        'otherparty_vehicle_registration', ]

class AccidentDetailsForm(ModelForm):
    class Meta:
        model = AccidentDetails
        widgets = {'police_report': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'date_of_accident': DateWidget(attrs={'id':"yourdateid"}, usel10n = True, bootstrap_version=3),
                   'time_of_accident': TimeWidget(attrs= {'id':"yourtimeid"}, usel10n = True, bootstrap_version=3),                    'incident_photos': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'witness': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'paramedics': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'emergency_treatment': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    'urgentcare_treatment': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                    }
        fields = ('client', 'date_of_accident', 'time_of_accident', 'weather_condition', 'city_of_accident', 'intersection_of_accident', 'police_report', 'police_report_number', 'accident_description',
                'incident_photos', 'witness', 'paramedics', 'emergency_treatment','er_facility_name', 'urgentcare_treatment', 'urgentcare_facility_name')

class AppointmentForm(forms.ModelForm):

    #appointment_date = forms.DateTimeField(widget = DateTimeWidget(usel10n = True, bootstrap_version = 3))
    class Meta:
        model = Appointment

        widgets = {'existing_client': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),
                   'appointment_date': DateWidget(attrs={'id':"yourdateid"}, usel10n = True, bootstrap_version=3),
                  'appointment_time': TimeWidget(attrs= {'id':"yourtimeid"}, usel10n = True, bootstrap_version=3)}
        fields = ('existing_client','caller_first_name', 'caller_last_name', 'type_of_appointment', 'further_appointment_notes', 'phone_number','appointment_date','appointment_time',)

class CallLogForm(forms.ModelForm):
    class Meta:
        model = CallLog

        widgets = {'call_date': DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3),
                    'date_of_accident':DateWidget(attrs={'id':"yourdateid"}, usel10n = True, bootstrap_version=3),}
        fields = ('client', 'date_of_accident', 'caller_name', 'caller_number', 'call_date','call_notes')

class DoctorInfoForm(forms.ModelForm):
    class Meta:
        model = DoctorInfo

        widgets = {'lien': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No")))}
        fields = ('client', 'hospital_name', 'hospital_number', 'lien')

class ClaimInfoForm(forms.ModelForm):
    class Meta:
        model = ClaimInfo

        fields = ('client', 'claim_number', 'adjuster_name', 'adjuster_phonenumber', 'adjuster_faxnumber', 'adjuster_address_1', 'adjuster_address_2', 'adjuster_city', 'adjuster_state', 'adjuster_zip_code')

class InsuranceInfoForm(forms.ModelForm):
    class Meta:
        model = InsuranceInformation
        widgets = {'rental_coverage': forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, "Yes"),(0, "No"))),}

        fields = ('client', 'insurance_company', 'policy_holder_name', 'policy_holder_name', 'policy_number', 'type_of_coverage', 'coverage_limit_pd', 'coverage_limit_medical', 'rental_coverage', 'perday_rental', 'deductible')

class OtherPartyInsuranceForm(forms.ModelForm):
    class Meta:
        model = InsuranceInformation
        fields = ('other_insurnace_company', 'other_Policy_holder_name', 'other_policy_number', 'other_type_of_coverage', 'other_policy_limit_pd', 'other_policy_limit')
