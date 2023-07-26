from django.shortcuts import render
from .forms import *

from django.contrib import messages
import csv
from io import TextIOWrapper


def dump_contacts(request, imported_contact_obj):
    required_fields = ['name', 'email']
    csv_text_wrapper = TextIOWrapper(imported_contact_obj.file.file, encoding='utf-8')

    with csv_text_wrapper as csvfile:
        reader = csv.DictReader(csvfile)
        column_names = [field.lower() for field in reader.fieldnames]
        print("Column Names:", column_names)

        if not all(field in column_names for field in required_fields):
            print("no")
            return "failed due to invalid fields"
        else:
            invalid_row_numbers = []
            for row_number, row in enumerate(reader, start=1):
                if not row['name'] or not row['email']:
                    invalid_row_numbers.append(row_number)

                else:
                    try:
                        user, created = User.objects.get_or_create(email = row['email'])
                        if created:
                            user.username = row['name']
                            user.set_password('test_password')
                            user.save()
                        profile = user.profile
                        profile.organization = request.user.profile.organization
                        profile.save()
                    except:
                        invalid_row_numbers.append(row_number)

            print(invalid_row_numbers)
            if len(invalid_row_numbers) > 0:
                log_msg = f'Invalid rows : {", ".join(str(e) for e in invalid_row_numbers)}'
                ImportedContactErrorLog.objects.create(imported_contact = imported_contact_obj, log_message = log_msg)
            

def import_contacts(request):
    form = ImportedContactForm()
    if request.method == 'POST':
        form = ImportedContactForm(request.POST, request.FILES)
        if form.is_valid():
            imported_contact_obj = form.save(commit=False)
            imported_contact_obj.uploaded_by = request.user.profile
            form.save()

            dump_contacts(request, imported_contact_obj)
            messages.success(request,"File uploaded!!")
        else:
            messages.error(request, "Something went worng while uploading the file")
    return render(request, 'Users/import_contact_form.html', context={'form':form})


def contact_import_logs(request):
    pass