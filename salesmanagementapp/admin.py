


from django.contrib import admin
from .models import ContactForm, ClientData, NewPropertyData, NewstatusData, NewPropertyTypeData, SendEnquiry, SoldProperty, PostReport

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']

class ClientDataAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_email', 'client_number', 'client_DOB', 'client_address1', 'client_address2', 'client_city', 'client_state', 'client_country']

class NewPropertyDataAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'property_type', 'status_name', 'property_cost', 'property_size', 'seller_contact_details', 'property_description']

class NewstatusDataAdmin(admin.ModelAdmin):
    list_display = ['seller_name', 'status_name', 'status_description']

class NewPropertyTypeDataAdmin(admin.ModelAdmin):
    list_display = ['seller_name', 'add_type_name', 'add_type_description']

class SendEnquiryAdmin(admin.ModelAdmin):
    list_display = ['seller_name', 'buyer_name', 'buy_mobile', 'buy_email', 'buy_dob', 'property_id', 'confirmation', 'sent_enquiry_on']

class SoldPropertyAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'property_type', 'status_name', 'property_cost', 'property_size', 'seller_contact_details', 'property_description', 'property_id', 'buyer_name']

class PostReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'property']

admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ClientData, ClientDataAdmin)
admin.site.register(NewPropertyData, NewPropertyDataAdmin)
admin.site.register(NewstatusData, NewstatusDataAdmin)
admin.site.register(NewPropertyTypeData, NewPropertyTypeDataAdmin)
admin.site.register(SendEnquiry, SendEnquiryAdmin)
admin.site.register(SoldProperty, SoldPropertyAdmin)
admin.site.register(PostReport, PostReportAdmin)
