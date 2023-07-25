from django.shortcuts import render
from .forms import *

from django.contrib import messages
import csv
from io import TextIOWrapper


def dump_contacts(file_instance):
    required_fields = ['name', 'email']
    csv_text_wrapper = TextIOWrapper(file_instance.file, encoding='utf-8')

    with csv_text_wrapper as csvfile:
        reader = csv.DictReader(csvfile)
        column_names = [field.lower() for field in reader.fieldnames]
        print("Column Names:", column_names)

        if not all(field in column_names for field in required_fields):
            print("no")
            return "failed due to invalid fields"
        else:
            print("yes")
            
        for row in reader:
            Profile.objects.create

# Create your views here.
def import_contacts(request):
    form = ImportedContactForm()
    if request.method == 'POST':
        form = ImportedContactForm(request.POST, request.FILES)
        if form.is_valid():
            imported_contact = form.save(commit=False)
            imported_contact.uploaded_by = request.user.profile
            form.save()

            dump_contacts(imported_contact.file)
            messages.success(request,"File uploaded!!")
        else:
            messages.error(request, "Something went worng while uploading the file")
    return render(request, 'Users/import_contact_form.html', context={'form':form})