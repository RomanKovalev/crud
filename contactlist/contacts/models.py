from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class ContactRecord(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    firstname = models.CharField(max_length=25, null=True, blank=True)
    lastname = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)


    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)