from django.shortcuts import render
from .models import Client, ClientAddress, ClientVehicle, ClientInstance, OtherPartyInformation, AccidentDetails, InsuranceInformation, Appointment
from django.views import generic
#from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import NewClientForm, ClientAddressForm, ClientVehicleForm, OtherPartyInfoForm, OtherPartyAddressForm, OtherPartyVehicleForm, AccidentDetailsForm, AppointmentForm, CallLogForm


# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_clients=Client.objects.all().count()
    num_instances=ClientInstance.objects.all().count()

    # Count based on case status: property damage
    num_instances_pd=ClientInstance.objects.filter(status__exact='propertydamage').count()
    #count based on case status: medical report pending
    num_instances_medical=ClientInstance.objects.filter(status__exact='pendingmedicalreport').count()

    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html',context={'num_clients':num_clients,'num_instances_pd':num_instances_pd,'num_instances_medical':num_instances_medical},)

def ClientListView(request):
    """
    View function for All clients page on the sidebar of site.
    """
    client_list = Client.objects.all()
    print (client_list)
    return render(request, 'client_list.html', {'client_list': client_list})

'''
class ClientListView(generic.ListView):
    model = Client
'''
class ClientDetailView(generic.DetailView):
    model = Client

def NewClient(request):
    """
    View function for signing up a new client
    """
    print("in add_new")
    client_inst = None
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("1st if")
        # Create a form instance and populate it with data from the request (binding):
        formA = NewClientForm(request.POST)
        formB = ClientAddressForm(request.POST)
        formC = ClientVehicleForm(request.POST)

        # Check if the form is valid:
        if formA.is_valid() and formB.is_valid() and formC.is_valid():
            client_inst = formA.save(commit=False)
            client_inst.save()
            client_address = formB.save(commit=False)
            client_address.save()
            client_vehicle = formC.save(commit=False)
            client_vehicle.save()
            #client_inst.groups.add(Group.objects.get(name='client'))
            print ("saved client")
            # redirect to a new URL:
            return client_list(request)
        else:
            print(formA.errors)

    # If this is a GET (or any other method) create the default form.
    else:
        formA = NewClientForm()
        formB = ClientAddressForm()
        formC = ClientVehicleForm()
        #proposed_statute_date = datetime.date_of_accident() + datetime.timedelta(years=2)
        #form = NewClientForm(initial={'statute_date': proposed_statute_date,})

    return render(request, 'new_client_signup.html', {'formA': formA, 'formB':formB, 'formC':formC})

def OtherParty(request):
    """
    View function for other party information
    """
    if request.method == 'POST':
        formA = OtherPartyInfoForm(request.POST)
        formB = OtherPartyAddressForm(request.POST)
        formC = OtherPartyVehicleForm(request.POST)

        if formA.is_valid() and formB.is_valid() and formC.is_valid():
            otherparty_inst = formA.save(commit=False)
            otherparty_inst.save()
            otherparty_address = formB.save(commit=False)
            otherparty_address.save()
            otherparty_vehicle = formC.save(commit=False)
            otherparty_vehicle.save()

            return otherparty_inst(request)
        else:
            print(formA.errors)

    # If this is a GET (or any other method) create the default form.
    else:
        formA = OtherPartyInfoForm()
        formB = OtherPartyAddressForm()
        formC = OtherPartyVehicleForm()
    return render(request, 'otherparty_info.html', {'formA': formA, 'formB': formB, 'formC': formC })

def AccidentDetails(request):
    if request.method == 'POST':
        formA = AccidentDetailsForm(request.POST)
        if formA.is_valid():
            accident_details = fromA.save(commit=False)
            accident_details.save()

            return accident_details(request)
        else:
            print (formA.errors)
    else:
        formA = AccidentDetailsForm()
    return render(request, 'accident_details.html', {'formA': formA})

def AppointmentDetails(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        print ("in appointment if")
        if form.is_valid():
            # Save the new category to the database.
            appointment_details = form.save(commit=False)
            appointment_details.save()

            # The user will be shown the appointment detail page view.
            print (appointment_details)
            return appointment_details(request)
        else:
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = AppointmentForm()

    # Render the form with error messages (if any)
    return render(request, 'appointment_details.html', {'form': form})

def AppointmentList(request):
    """
    View function for All appointments.
    """
    appointment_list = Appointment.objects.all()
    print (appointment_list)
    return render(request, 'appointment_list.html', {'appointment_list': appointment_list})

def CallLog(request):
    if request.method =='POST':
        form = CallLogForm(request.POST)
        if form.is_valid():
            call_details = form.save(commit=False)
            call_details.save()
        else:
            print(form.errors)
    else:
        form = CallLogForm()

    return render(request, 'call_details.html', {'form': form})
