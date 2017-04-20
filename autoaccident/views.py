from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Client, ClientAddress, ClientVehicle, ClientInstance, OtherPartyInformation, AccidentDetails, InsuranceInformation, Appointment, DoctorInfo, CallLog, InsuranceInformation, ClaimInfo
from django.views import generic
from django.contrib.auth.models import User, Group, Permission
#from django.contrib.auth.decorators import permission_required

#from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime
from django.contrib.auth.decorators import login_required
from .forms import NewClientForm, ClientAddressForm, ClientVehicleForm, OtherPartyInfoForm, OtherPartyAddressForm, OtherPartyVehicleForm, AccidentDetailsForm, AppointmentForm, CallLogForm, DoctorInfoForm, ClaimInfoForm, InsuranceInfoForm, OtherPartyInsuranceForm


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

def index_attorney(request):

    return render(request, 'index_attorney.html')



'''
class ClientListView(generic.ListView):
    model = Client
'''
class ClientDetailView(generic.DetailView):
    model = Client

@login_required
def AddClient(request):
    """
    View function for signing up a new client
    """
    print("in add_new")
    print ("Request method is: ", str(request.method))
    client_inst = None
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("1st if")
        # Create a form instance and populate it with data from the request (binding):
        form = NewClientForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            client_inst = form.save(commit=False)
            client_inst.save()

            #client_inst.groups.add(Group.objects.get(name='client'))
            print ("saved client")
            # redirect to a new URL:
            return client_list(request)
        else:
            print(form.errors)


    # If this is a GET (or any other method) create the default form.
    else:
        form = NewClientForm()

        #proposed_statute_date = datetime.date_of_accident() + datetime.timedelta(years=2)
        #form = NewClientForm(initial={'statute_date': proposed_statute_date,})

    return render(request, 'add_client.html', {'form': form})

@login_required
def NewClient(request):
    """
    View function for signing up a new client
    """
    print("in add_new")
    print ("Request method is: ", str(request.method))
    client_inst = None
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        print("1st if")
        # Create a form instance and populate it with data from the request (binding):
        #formA = NewClientForm(request.POST)
        formB = ClientAddressForm(request.POST)
        formC = ClientVehicleForm(request.POST)
        formD = DoctorInfoForm(request.POST)
        formE = ClaimInfoForm(request.POST)
        formF = AccidentDetailsForm(request.POST)
        formG = InsuranceInfoForm(request.POST)

        # Check if the form is valid:
        if formB.is_valid() and formC.is_valid() and formD.is_valid() and formE.is_valid() and formF.is_valid() and formG.is_valid():

            client_address = formB.save(commit=False)
            #client_address.client = client_inst
            client_address.save()
            client_vehicle = formC.save(commit=False)
            #client_vehicle.client = client_inst
            client_vehicle.save()
            doctor_info = formD.save(commit=False)
            #doctor_info.client = client_inst
            doctor_info.save()
            claim_info = formE.save(commit=False)
            claim_info.save()
            treatment_info = formF.save(commit=False)
            treatment_info.save()
            insurance_info = formG.save(commit=False)
            insurance_info.save()
            #client_inst.groups.add(Group.objects.get(name='client'))
            print ("saved client")
            # redirect to a new URL:
            return client_detail(request)
        else:

            print("Validation Failed with errors formB: ", formB.errors)
            print("Validation Failed with errors formC: ", formC.errors)
            print("Validation Failed with errors formD: ", formD.errors)

            if formB.is_valid():
                print("I can create Address")
                client_address = formB.save(commit=False)
                client_address.save()
            if formC.is_valid():
                print("I can create vehicle")
                client_vehicle = formC.save(commit=False)
                client_vehicle.save()
            if formD.is_valid():
                print("I can create Doctor")
                doctor_info = formD.save(commit=False)
                doctor_info.save()

    # If this is a GET (or any other method) create the default form.
    else:
        #formA = NewClientForm()
        formB = ClientAddressForm()
        formC = ClientVehicleForm()
        formD = DoctorInfoForm()
        formE = ClaimInfoForm()
        formF = AccidentDetailsForm()
        formG = InsuranceInfoForm()
        #proposed_statute_date = datetime.date_of_accident() + datetime.timedelta(years=2)
        #form = NewClientForm(initial={'statute_date': proposed_statute_date,})

    return render(request, 'new_client_signup.html', {'formB':formB, 'formC':formC, 'formD':formD, 'formE':formE, 'formF':formF, 'formG':formG})

@login_required
def ClientListView(request):
    """
    View function for All clients page on the sidebar of site.
    """
    client_list = Client.objects.all()
    client_count = Client.objects.all().count()

    return render(request, 'client_list.html', {'client_list': client_list, 'client_count':client_count})

@login_required
def ChristmasListView(request):
    """
    View function for All clients page on the sidebar of site.
    """
    christmas_list = Client.objects.all()
    client_address = ClientAddress.objects.all()
    print (client_address)
    return render(request, 'christmas_list.html', {'christmas_list': christmas_list, 'address': client_address})

@login_required
def OtherParty(request):
    """
    View function for other party information
    """
    if request.method == 'POST':
        formA = OtherPartyInfoForm(request.POST)
        formB = OtherPartyAddressForm(request.POST)
        formC = OtherPartyVehicleForm(request.POST)
        formD = OtherPartyInsuranceForm(request.POST)

        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid():
            otherparty_inst = formA.save(commit=False)
            otherparty_inst.save()
            otherparty_address = formB.save(commit=False)
            otherparty_address.save()
            otherparty_vehicle = formC.save(commit=False)
            otherparty_vehicle.save()
            otherparty_insurance = formD.save(commit=False)
            otherparty_insurance.save()

            return otherparty_inst(request)
        else:
            print(formA.errors)

    # If this is a GET (or any other method) create the default form.
    else:
        formA = OtherPartyInfoForm()
        formB = OtherPartyAddressForm()
        formC = OtherPartyVehicleForm()
        formD = OtherPartyInsuranceForm()
    return render(request, 'otherparty_info.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD})

@login_required
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

@login_required
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

@login_required
def AppointmentList(request):
    """
    View function for All appointments.
    """
    appointment_list = Appointment.objects.all()
    print ("in appointment list")
    print (appointment_list[1].appointment_date)
    return render(request, 'appointment_list.html', {'appointment_list': appointment_list})

@login_required
def CallLogView(request):
    if request.method =='POST':
        form = CallLogForm(request.POST)
        if form.is_valid():
            call_details = form.save(commit=False)
            call_details.save()
        else:
            print(form.errors)
    else:
        form = CallLogForm()

    return render(request, 'call_log.html', {'form': form})

@login_required
def CallList(request):
    """
    View function for All appointments.
    """
    call_list = CallLog.objects.all()
    return render(request, 'call_list.html', {'call_list': call_list})


def DoctorInfoView(request):
    if request.method =='POST':
        form = DoctorInfoForm(request.POST)
        if form.is_valid():
            doctor_details = form.save(commit=False)
            doctor_details.save()
        else:
            print(form.errors)
    else:
        form = DoctorInfoForm()

    return render(request, 'doctor_details.html', {'form': form})


def ClaimInfoView(request):
    if request.method =='POST':
        form = ClaimInfoForm(request.POST)
        if form.is_valid():
            claim_details = form.save(commit=False)
            claim_details.save()
        else:
            print(form.errors)
    else:
        form = ClaimInfoForm()

    return render(request, 'new_client_signup.html', {'form': form})

def ClientDetail(request, pk):
    print("In ClientDetail. PK is: ", str(pk))
    client_profile = Client.objects.get(id=pk)


    client_address= ClientAddress.objects.get(client_id=pk)
    print ("Client Address: ", client_address.city)
    client_vehicle = ClientVehicle.objects.get(client_id=pk)
    treatment_info = DoctorInfo.objects.get(client_id=pk)
    print ("Client treatment: ", treatment_info.hospital_name)
    #accident_details = AccidentDetails.objects.get(client_id=pk)
    #Insurance_info = InsuranceInformation.objects.get(client_id=pk)
    #otherparty_info = OtherPartyInformation.objects.filter(client_id=pk)
    context_dict = {'profile': client_profile, 'address': client_address, 'vehicle': client_vehicle, 'treatment': treatment_info}
    print("in client profile")
    return render(request, 'client_detail.html', context_dict)

def EditClient(request, pk):
    if request.method == 'POST':
        formA = NewClientForm(request.POST)
        formB = ClientAddressForm(request.POST)
        formC = ClientVehicleForm(request.POST)
        formD = DoctorInfoForm(request.POST)

        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid():
            # Save the new category to the database.

            client_inst = formA.save()
            client_address = formB.save(commit=False)
            clientaddress.client = clientUser
            clientaddress.save()
            client_vehicle = formC.save(commit = False)
            client_vehicle.client = clientUser
            client_vehicle.save()
            doctor_info = formD.save(commit = False)
            doctor_info.client = clientUser
            doctor_info.save()
            clientUser.groups.add(Group.objects.get(name='client'))
            print("saved new client")

            # The user will be shown the patient profile page view.
            return client_detail(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(formA.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        formA = NewClientForm()
        formB = ClientAddressForm()
        formC = ClientVehicleForm()
        formD = DoctorInfoForm()

    # Render the form with error messages (if any), if no form supplied
    return render(request, 'edit_client.html', {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD})

@login_required
def Analytics(request):
    #data_content = str("[{type: \"column\",dataPoints: [{ label: \"apple\",  y: 10  },{ label: \"orange\", y: 15  },{ label: \"banana\", y: 25  },{ label: \"mango\",  y: 30  },{ label: \"grape\",  y: 28  }]}]")
    data_content = """[{type: "column",dataPoints: [{ label: "apple",  y: 10  },{ label: "orange", y: 15  },{ label: "banana", y: 25  },{ label: "mango",  y: 30  },{ label: "grape",  y: 28  }]}]"""
    print (data_content)
    return render(request, 'testgraph.html',{'data_content': data_content})


def InsuranceInfoView(request):
    if request.method =='POST':
        form = InsuranceInfoForm(request.POST)
        if form.is_valid():
            insurance_details = form.save(commit=False)
            insurance_details.save()
        else:
            print(form.errors)
    else:
        form = InsuranceInfoForm()

    return render(request, 'insurance_info.html', {'form': form})
