from django.urls import path
from .views import *


urlpatterns = [
    path('import_contacts/', import_contacts, name='import_contacts'),
]
