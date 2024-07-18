from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.core.files.uploadedfile import TemporaryUploadedFile

from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from scopetoproposal.serializers import ClientSerializer, FileUploadSerializer
from scopetoproposal.models import Client

from utils.proposal import create_proposal


# Create your views here.

def healthz(request):
    return HttpResponse(status=status.HTTP_200_OK)


def maintenance(request):
    return render(request, 'scopetoproposal/maintenance.html')




class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('created')
    serializer_class = ClientSerializer



# A class to convert PDF from user-point to word with utils function

def upload_page(request):
    return render(request, 'scopetoproposal/upload.html')


class FileUploadView(APIView):
    """
    API endpoint that takes PDF file input and runs this through utils.proposal for DOCX output
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        proposal_file = 'utils/file.docx'
        match request.FILES['proposal'].name:
            # no extra directors:
            case 'SITE HEALTH AND SAFETY MANAGEMENT IN RESPECT OF CLIENT.docx':
                proposal_file = 'utils/client.docx'
            case 'SITE HEALTH AND SAFETY MANAGEMENT IN RESPECT OF PERMIT APPLICATION CLIENT.docx':
                proposal_file = 'utils/permit_application_client.docx'
            # extra directors:
            case 'SITE HEALTH AND SAFETY MANAGEMENT IN RESPECT OF PC.docx':
                proposal_file = 'utils/pc.docx'
            case 'SITE HEALTH AND SAFETY MANAGEMENT IN RESPECT OF PC RETAINER.docx':
                proposal_file = 'utils/pc_retainer.docx'
            case 'SITE HEALTH AND SAFETY MANAGEMENT IN RESPECT OF MOBI PACK.docx':
                proposal_file = 'utils/mobi_pack.docx'

        company = request.data['company']

        scope_serializer = FileUploadSerializer(data={'file': request.FILES['scope']})
        proposal_serializer = FileUploadSerializer(data={'file': request.FILES['proposal']})
        if scope_serializer.is_valid() and proposal_serializer.is_valid():
            with open(proposal_file, 'wb+') as destination:
                for chunk in request.FILES['proposal'].chunks():
                    destination.write(chunk)
            output = create_proposal(request.FILES['scope'], proposal_file, company)
        
        # TEMP something keeps downloading documents
        # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response = FileResponse(open(output, 'rb'))
        # response = FileResponse(output)
        return response








# @api_view
def test(request):
    ...
    print('You have reached TEST')

    return HttpResponse(200)

