from django.db import models
from datetime import date, datetime
from django.utils import timezone
from datetimewidget.widgets import DateWidget, DateTimeWidget, TimeWidget
#from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField
from localflavor.us.us_states import STATE_CHOICES
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # required for unique client instance

# Create your models here.
'''
class Incident(models.Model):
    # model representing the the type of incident the client is involved in, eg. autoaccident
    INCIDENT_CHOICES = (('autoaccident', 'Autoaccident'), ('slip and fall', 'Slip and Fall'), ('other', 'Other'))
    ACCIDENT_CHOICES = (('rearended', 'RearEnded'), ('headon collision', 'Headon Collision'))
    incident_type = models.CharField(max_length=50, help_text="Enter the type of incident")
    summary = models.TextField(max_length=1000, help_text='Enter a short description of the incident')
    def __str__(self):
       """
       String for representing the Model object (in Admin site etc.)
       """
       return str(self.incident_type)
'''

class Client(models.Model):
    # model representing the client of the lawfirm eg. driver, passenger

    CLIENT_CHOICES = (('driver', 'Driver'), ('passenger', 'Passenger'), ('slipflall', 'Slipfall'), ('other', 'Other'))
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True)
    client_type = models.CharField(max_length=50, choices=CLIENT_CHOICES, null=True)
    phone_number = models.CharField(max_length=10, null = True)
    date_of_birth = models.DateField(_("Date of Birth"), null = True)
    driver_license = models.CharField(max_length=8, null = True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null = True)
    ssnumber = models.CharField(max_length=9, null = True)
    medicare_coverage = models.BooleanField(default=False, help_text='Are you covered by Medicare?')
    medicaid_coverage = models.BooleanField(default=False, help_text='Are you covered by Medicaid?')
    date_of_accident = models.DateField(_("Date of Accident"), null=True)
    passengers = models.BooleanField(default=False, help_text='Any passengers in the car?' )
    number_of_passengers = models.IntegerField(null=True, blank=True)
    injuries = models.TextField(max_length=100, null=True, help_text='list the injuries,eg. neck, back etc.')
    #incident = models.OneToOneField(Incident, help_text='Select a type of incident for the client')
    #OneToOneField used becasue a client can involved in only one type of incident at a time


    def __str__(self):

        return str(self.first_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('client-detail', args=[str(self.id)])

class ClientAddress(models.Model):
    # model representing the client's address
    client = models.OneToOneField(Client, help_text='select client', null=True)
    address_1 = models.CharField(_("address"), max_length=128, blank = True)
    address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64, default="Fullerton", null=True)
    state = USStateField(choices=STATE_CHOICES, default="CA")
    zip_code = models.CharField(_("zip code"), max_length=5, blank=True)


    def __str__(self):

        return str(self.client.first_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('clientaddress-detail', args=[str(self.id)])


class ClientVehicle(models.Model):
    #model representing the vehicle client was driving during the accident.
    client = models.OneToOneField(Client, help_text='select client', null=True)
    vehicle_year=models.CharField(max_length=4, null=True)
    vehicle_make=models.CharField(max_length=50, null=True)
    vehicle_model=models.CharField(max_length=50, null=True)
    vehicle_registration=models.CharField(max_length=7, null=True)
    vehicle_color=models.CharField(max_length=50, null=True)
    carseat=models.NullBooleanField()
    damage_location=models.TextField(max_length=100, help_text='Enter where the damage is on the vehicle', null=True)
    damage_description=models.TextField(max_length=400, help_text='Enter a description of the damage', null=True)


    def __str__(self):

        return str(self.client.first_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('clientvehicle-detail', args=[str(self.id)])

class ClientInstance(models.Model):
    # model representing individual client for a specific accident as same client can have multiple accidents

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular client across whole site")
    client = models.ForeignKey('Client', null=True)
    CASE_STATUS = (('signinpending', 'Signin Pending'),
                    ('propertydamage', 'Property Damage'),
                    ('pendingmedicalreport', 'Pending Medical Report'),
                    ('demand', 'Demand'),
                    ('reject-1', 'Reject-1'),
                    ('reject-2', 'Reject-2'),
                    ('reject-3', 'Reject-3'),
                    ('pendingfiling', 'Pending Filing in Court'),
                    ('filed-in-court', 'Filed in Court'),
                    ('closed', 'Closed'),
                    ('other', 'Other'))

    status = models.CharField(max_length=50, choices=CASE_STATUS, blank=True, default='pending', help_text='Case Status' )

    def __str__(self):
        return '%s (%s)' % (self.id,self.client.first_name)

class OtherPartyInformation(models.Model):
    # model to represent the inofrmation of the other parties involved.

    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
    #following is other party's personal information
    client = models.ForeignKey('Client', null=True)
    otherparty_driver_name = models.CharField(max_length=100, null=True, blank=True)
    otherparty_phonenumber = models.CharField(max_length=10, null = True)
    otherparty_date_of_birth = models.DateField(_("Date of Birth"), null = True)
    otherparty_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null = True)
    otherparty_driver_license = models.CharField(max_length=8, null = True)
    #otherparty_number_of_passengers = models.IntegerField(null=True, blank=True)
    # following is other party's address details.

    otherparty_address_1 = models.CharField(_("address"), max_length=128, blank = True)
    otherparty_address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    otherparty_city = models.CharField(_("city"), max_length=64, default="Fullerton", null=True)
    otherparty_state = USStateField(choices=STATE_CHOICES, default="CA")
    otherparty_zip_code = models.CharField(_("zip code"), max_length=5, blank=True)

    # following is other party's vehicle details.

    otherparty_vehicle_year=models.CharField(max_length=4, null=True)
    otherparty_vehicle_make=models.CharField(max_length=50, null=True)
    otherparty_vehicle_model=models.CharField(max_length=50, null=True)
    otherparty_vehicle_registration=models.CharField(max_length=7, null=True)
    otherparty_vehicle_color=models.CharField(max_length=50, null=True)
    #otherparty_damage_location=models.TextField(max_length=100, help_text='Enter where the damage is on the vehicle', null=True)
    #otherparty_damage_description=models.TextField(max_length=400, help_text='Enter a description of the damage', null=True)


    def __str__(self):

        return str(self.otherparty_driver_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('otherparty-detail', args=[str(self.id)])

class AccidentDetails(models.Model):
# model representing the details of the incident, and police report.

    CLIMATE_CHOICES = (('normal', 'Normal'),
                        ('cloudy', 'Cloudy'),
                        ('rainy', 'Rainy'),
                        ('foggy','Foggy'),
                        ('windy','Windy')
                        )

    client = models.ForeignKey('Client', null=True)
    date_of_accident = models.DateTimeField(blank=True, null=True)
    time_of_accident = models.TimeField(blank=True, null=True)
    weather_condition = models.CharField(max_length=20, choices=CLIMATE_CHOICES, null=True)

    city_of_accident = models.CharField(_("city"), max_length=64, default="Fullerton", null=True, blank=True)
    intersection_of_accident = models.CharField(max_length=150, help_text='Provide the name of the street where the incident took place', null=True, blank=True)
    police_report = models.BooleanField(default=False, help_text='Did the police make a incident report?')
    police_report_number = models.CharField(max_length=15, null=True, blank=True)
    accident_description = models.TextField(max_length=1000, null=True, help_text='Please enter a brief description of how the accident happened')
    incident_photos = models.BooleanField(default=False, help_text='Pictures of the incident and/or vehicle?')
    witness = models.BooleanField(default=False, help_text='Are there any witnesses of the incident?')

    # following are emergency treatment details
    paramedics = models.BooleanField(default=False, help_text='Paramedics come to the scene of accident?')
    emergency_treatment = models.BooleanField(default=False, help_text='Were you transported to ER?')
    er_facility_name = models.CharField(max_length=20, null=True, blank=True, help_text='Name of the ER hospital', default='N/A')

    #following are urgent care treatment details
    urgentcare_treatment = models.BooleanField(default=False, help_text='Did the clientgo to any urgent care?')
    urgentcare_facility_name = models.CharField(max_length=20, null=True, blank=True, help_text='Name of the urgentcare hospital', default='N')

    def __str__(self):

        return str(self.city_of_accident)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('accident-detail', args=[str(self.id)])


class InsuranceInformation(models.Model):
    # model representing the details of the adjuster assigned to the case by the insurance company
    client = models.ForeignKey('Client', null=True)

    COVERAGE_CHOICES = (('Liability only', 'liability only'),
                        ('Comprehensive Coverage', 'comprehensive coverage'),
                        ('Collision Coverage', 'collision coverage'),
                        ('Uninsured/Underinsured Motorist', 'uninsured/underinsured motorist'),
                        ('Medical Payments', 'medical payments'),
                        ('Personal Injury Protection', 'personal injury protection'))

    # Attributes for own insursnce information
    insurance_company = models.CharField(max_length=50, null=True)
    policy_holder_name = models.CharField(max_length=30, null=True)
    policy_number = models.CharField(max_length=15, null=True)
    type_of_coverage = models.CharField(max_length=50, choices=COVERAGE_CHOICES, null = True)
    coverage_limit_pd = models.CharField(max_length=8, null=True,help_text='Enter the policy limit for property damage in dollars')
    coverage_limit_medical = models.CharField(max_length=8, null=True, help_text='Enter the policy limit for medical in dollars')
    rental_coverage = models.BooleanField(default=False, help_text='Does clients insurance cover rental vehicle?')
    perday_rental = models.CharField(max_length=7, null=True, blank=True, help_text='Rental coverage per day in dollars')
    deductible = models.CharField(max_length=7, null=True, blank=True, help_text='collision coverage deductible in dollars')
    # Attributes for other party's insurance information

    other_insurnace_company = models.CharField(max_length=20, null=True)
    other_Policy_holder_name = models.CharField(max_length=30, null=True)
    other_policy_number = models.CharField(max_length=15, null=True)
    other_type_of_coverage = models.CharField(max_length=20, choices=COVERAGE_CHOICES, null = True)
    other_policy_limit_pd = models.CharField(max_length=8, null=True, help_text='Enter the policy limit for property damage in dollars')
    other_policy_limit = models.CharField(max_length=8, null=True, help_text='Enter the policy limit per incident in dollars')

    def __str__(self):

        return str(self.insurnace_company)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('accident-detail', args=[str(self.id)])

class Appointment(models.Model):

    APPOINTMENT_CHOICES = (('New Case', 'New Case',),
                            ('Existing Case', 'Existing Case',),
                            ('Property Damage Discussion', 'Property Damage Discussion'),
                            ('Medical Report', 'Medical Report'),
                            ('Documents Signing', 'Documents Signing'),
                            ('Documents Subminssion', 'Documents Subminssion'),
                            ('Discussing the Settlement Offer', 'Discussing the Settlement Offer'),
                            ('To sign the settlement Documents', 'To sign the settlement Documents'),
                            ('Check Collection', 'Check Collection'),
                            ('For Case Status', 'For Case Status'),
                            ('Other', 'Other'),)

    existing_client = models.BooleanField(default=False, help_text='Existing client?' )
    caller_first_name = models.CharField(max_length=50, null=True)
    caller_last_name = models.CharField(max_length=50, null=True)
    type_of_appointment = models.CharField(max_length=100, choices=APPOINTMENT_CHOICES, null = True)
    further_appointment_notes = models.TextField(max_length=50, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    appointment_date = models.DateTimeField(
            blank=True, null=True)
    appointment_time = models.TimeField(
            blank=True, null=True)
    #cancel = models.NullBooleanField()

    def __str__(self):
        return str(self.caller_first_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('appointment-detail', args=[str(self.id)])

class CallLog(models.Model):
    # model to track the phone call made and received regarding the case
    client = models.ForeignKey('Client', null=True)
    date_of_accident = models.DateTimeField(blank=True, null=True)
    caller_name = models.CharField(max_length=100, null=True)
    caller_number = models.CharField(max_length=10, null = True)
    call_date = models.DateTimeField(default=datetime.now,
            blank=True, null=True)
    call_notes = models.TextField(max_length=100, null=True)

    def __str__(self):
        return str(self.caller_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('call-detail', args=[str(self.id)])


class DoctorInfo(models.Model):
    client = models.ForeignKey('Client', null=True)

    hospital_name = models.CharField(max_length=50, null=True)
    hospital_number = models.CharField(max_length=10, null = True)
    lien = models.BooleanField(default=False, help_text='lien signed?')

    def __str__(self):
        return str(self.hospital_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('doctor-detail', args=[str(self.id)])


class ClaimInfo(models.Model):
    client = models.ForeignKey('Client', null=True)

    claim_number = models.CharField(max_length=20, null=True)
    adjuster_name = models.CharField(max_length=20, null = True)
    adjuster_phonenumber = models.CharField(max_length=10, null = True)
    adjuster_faxnumber = models.CharField(max_length=10, null=True)

    #following are insurance adjuster address information

    adjuster_address_1 = models.CharField(_("address"), max_length=128, blank = True)
    adjuster_address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    adjuster_city = models.CharField(_("city"), max_length=64, default="Fullerton", null=True)
    adjuster_state = USStateField(choices=STATE_CHOICES, default="CA")
    adjuster_zip_code = models.CharField(_("zip code"), max_length=5, blank=True)


    def __str__(self):
        return str(self.claim_number)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('claim-detail', args=[str(self.id)])

class OtherPartyClaim(models.Model):
    client = models.ForeignKey('Client', null=True)

    claim_number = models.CharField(max_length=20, null=True)
    adjuster_name = models.CharField(max_length=20, null = True)
    adjuster_phonenumber = models.CharField(max_length=10, null = True)
    adjuster_faxnumber = models.CharField(max_length=10, null=True)

    #following are insurance adjuster address information

    adjuster_address_1 = models.CharField(_("address"), max_length=128, blank = True)
    adjuster_address_2 = models.CharField(_("address cont'd"), max_length=128, blank=True)
    adjuster_city = models.CharField(_("city"), max_length=64, default="Fullerton", null=True)
    adjuster_state = USStateField(choices=STATE_CHOICES, default="CA")
    adjuster_zip_code = models.CharField(_("zip code"), max_length=5, blank=True)


    def __str__(self):
        return str(self.claim_number)

    def get_absolute_url(self):
        """
        Returns the url to access a particular client instance.
        """
        return reverse('claim-detail', args=[str(self.id)])

class CourtCase(models.Model):
    client = models.ForeignKey('Client', null=True)

    case_number = models.CharField(max_length=20, null=True)
    trial_Date = models.DateTimeField(
            blank=True, null=True)
    osc_date = models.DateTimeField(
            blank=True, null=True)
    cmc_date = models.DateTimeField(
            blank=True, null=True)
    depo_date = models.DateTimeField(
            blank=True, null=True)
    mediation_date = models.DateTimeField(
            blank=True, null=True)
    arbitration_date = models.DateTimeField(
            blank=True, null=True)
    final_status_conference = models.DateTimeField(
            blank=True, null=True)
    trial_setting_conf_date = models.DateTimeField(
            blank=True, null=True)
