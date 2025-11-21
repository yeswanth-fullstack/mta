from django.contrib import admin

# Register your models here.
from .models import TransactionSummary

admin.site.register(TransactionSummary)
