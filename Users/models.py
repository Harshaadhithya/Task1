from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=250, unique=True)
    #other fields.....

    def __str__(self):
        return self.name
    

class UserRole(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True, blank=True)
    mobile = models.PositiveBigIntegerField(null=True, blank=True)
    extra_fields = models.JSONField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.role:
            default_role, created = UserRole.objects.get_or_create(name='Contact')
            self.role = default_role
        super().save(*args, **kwargs)


    def __str__(self):
        return self.email
    

class ImportedContact(models.Model):
    status_choices = (
        ('Invalid', 'Invalid'),
        ('In Progress', 'In Progress'),
        ('Import Failed', 'Import Failed'),
        ('Import Success', 'Import Success')
    )
    uploaded_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    # organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='imported_contacts_CSV')
    status = models.CharField(max_length=30, choices=status_choices, default='In Progress')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.uploaded_by and self.uploaded_by.organization:
            return f'{self.uploaded_by.email}-{self.uploaded_by.organization.name}'
        else:
            return f'{self.file}'
    