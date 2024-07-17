from rest_framework import serializers
from scopetoproposal.models import INDUSTRIES, Client, Company


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['url', 'id', 'company_name', 'contact_person', 'contact_email', 'contact_number', 'industry']




class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()



class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'tel']
