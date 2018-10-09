from django.contrib import admin
from .models import Transactions, Users, Description

# Register your models here.

admin.site.register(Transactions)
admin.site.register(Users)
admin.site.register(Description)