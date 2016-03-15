from django.contrib import admin
from invoices.models import Invoice, Transcation

# Register your models here.
model_list = [Invoice, Transcation]
admin.site.register(model_list)
