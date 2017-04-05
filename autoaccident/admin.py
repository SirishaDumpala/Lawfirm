from django.contrib import admin
from .models import Client, ClientAddress, ClientVehicle, ClientInstance

# Register your models here.
'''
admin.site.register(Incident)
admin.site.register(Client)
admin.site.register(ClientAddress)
admin.site.register(ClientVehicle)
'''
# register the class using the decorator and define admin class

class ClientsInstanceInline(admin.TabularInline):
    model = ClientInstance

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'client_type', 'phone_number')
    inlines = [ClientsInstanceInline]

@admin.register(ClientAddress)
class ClientAddressAdmin(admin.ModelAdmin):
    list_display = ('client', 'address_1', 'city', 'zip_code')


'''
class ClientsVehicleInline(admin.TabularInline):
    model = ClientVehicle
'''
@admin.register(ClientVehicle)
class ClientVehicleAdmin(admin.ModelAdmin):
    list_display = ('client', 'vehicle_year', 'vehicle_make', 'vehicle_model', 'damage_location')
    fields = ['client', ('vehicle_year', 'vehicle_make', 'vehicle_model')]
    #inlines = [ClientsVehicleInline]
'''
@admin.register(ClientInstance)
class ClientInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'Statute_of_limitation')
'''
