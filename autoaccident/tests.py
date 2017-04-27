from django.test import TestCase

# Create your tests here.

from .models import Client, ClientAddress, ClientVehicle, AccidentDetails, OtherPartyInformation, Appointment
import datetime
from django.shortcuts import render, redirect, render_to_response

class ClientModelTest(TestCase):

    @classmethod
    def setUp(self):
        #Set up non-modified objects used by all test methods
        Client.objects.create(first_name='Big', last_name='Bob')
        Client.objects.create(first_name='John', last_name='Johnson', gender='male',date_of_accident='2017-03-08')
        Client.objects.create(first_name='David', last_name='Smith', gender='male',date_of_accident='2017-01-25',ssnumber='999999999')
        ClientAddress.objects.create(client_id=1,address_1='9950 juanita st',city='Anaheim',state='CA',zip_code='92801')
        ClientVehicle.objects.create(client_id=1,vehicle_make='Honda',vehicle_model='civic',vehicle_year='2000',vehicle_color='colorless',damage_location='front')
        AccidentDetails.objects.create(client_id=1,weather_condition='normal',paramedics='True')
        OtherPartyInformation.objects.create(client_id=1,otherparty_phonenumber='7147681998',otherparty_driver_license='D1234567',otherparty_date_of_birth='1980-01-01')


    def test_first_name_label(self):
        client=Client.objects.get(id=1)
        field_label = client._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')


    def test_first_name_max_length(self):
        client=Client.objects.get(id=1)
        max_length = client._meta.get_field('first_name').max_length
        self.assertEquals(max_length,50)

    def test_first_name(self):
        client=Client.objects.get(id=1)
        #This will also fail if the urlconf is not defined.

        self.assertEquals(client.first_name,'Big')

    def test_gender(self):
        client = Client.objects.get(id=2)
        self.assertEquals(client.gender,'male')

    def test_address(self):
        address = ClientAddress.objects.get(client_id=1)
        self.assertEquals(address.city,'Anaheim')

    def test_vehicle(self):
        vehicle = ClientVehicle.objects.get(client_id=1)
        self.assertEquals(vehicle.vehicle_make,'Honda')
        self.assertEquals(vehicle.vehicle_model,'civic')
        self.assertEquals(vehicle.vehicle_year,'2000')
        self.assertEquals(vehicle.damage_location,'front')

    def test_accidentdetails(self):
        accident = AccidentDetails.objects.get(client_id=1)
        self.assertEquals(accident.weather_condition,'normal')
        self.assertEquals(accident.paramedics, True)

    def test_otherparty(self):
        otherparty = OtherPartyInformation.objects.get(client_id=1)
        self.assertEquals(otherparty.otherparty_phonenumber,'7147681998')
        self.assertEquals(otherparty.otherparty_driver_license,'D1234567')
        self.assertEquals(otherparty.otherparty_date_of_birth,datetime.date(1980, 1, 1))
'''
    def test_load_client_list(request):
            client_list = {'client': Client.objects.all()}
            return render(request, '/client_list.html', client_list)
'''
class AppointmentModelTest(TestCase):

    @classmethod
    def setUp(self):
        Appointment.objects.create(caller_first_name='Tom', caller_last_name='Cruise')

    def test_name(self):
        appointment=Appointment.objects.get(id=1)
        #This will also fail if the urlconf is not defined.

        self.assertEquals(appointment.caller_first_name,'Tom')
        self.assertEquals(appointment.caller_last_name,'Cruise')
