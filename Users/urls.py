from django.urls import path
from .views import *


urlpatterns = [
    path('import_contacts/', import_contacts, name='import_contacts'),
    path('contact_import_logs/',contact_import_logs, name='contact_import_logs'),
]
