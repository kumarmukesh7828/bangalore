from django.contrib import admin
from .models import Vendor, VendorAddress

# Register your models here.
admin.site.register(Vendor)
admin.site.register(VendorAddress)
