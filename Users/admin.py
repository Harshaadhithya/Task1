from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(UserRole)
admin.site.register(Organization)
admin.site.register(ImportedContact)
admin.site.register(ImportedContactErrorLog)
