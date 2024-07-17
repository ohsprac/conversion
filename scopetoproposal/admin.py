from django.contrib import admin

from .models import Image, Company

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel')




admin.site.register(Image, ImageAdmin)
admin.site.register(Company, CompanyAdmin)