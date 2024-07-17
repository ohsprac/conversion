from django.db import models

# Create your models here.


INDUSTRIES = [('N', 'None'), ('Con', 'Construction'), ('Com', 'Commercial'), ('Eng', 'Eergy'), ('Pet', 'PetroChemical')]


class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=100, blank=True, default='')
    contact_person = models.CharField(max_length=100, blank=True, default='')
    contact_email = models.EmailField(max_length=100, blank=True, default='')
    contact_number = models.CharField(max_length=100, blank=True, default='')
    industry = models.CharField(choices=INDUSTRIES, default='N', max_length=100)

    class Meta:
        ordering = ['created']




class Image(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)




class Company(models.Model):
    name = models.CharField(max_length=200, blank=True)
    tel = models.CharField(max_length=200, blank=True, default='(011) 425 6352')

