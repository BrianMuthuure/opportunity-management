from django.contrib import admin

# Register your models here.
from main.models import Account, Opportunity

admin.site.register(Account)
admin.site.register(Opportunity)