from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from ftplib import FTP
import json
import shutil
from django.http import HttpResponse
from django.utils.encoding import smart_str


class SystemView(APIView):

    def post (self, request ,services ,format = None):
        file = request.FILES['file']
        dict_file = {}
        dict_file['file'] = file
        if services == 'pdftoinvoice':
            serializer = PDFToInvoiceSerializer(data=dict_file)
        elif services == 'bi':
            serializer =  BISerializer(data=dict_file)
        elif services == 'frontend':
            serializer = FrontEndSerializer(data=dict_file)
        elif services == 'management':
            serializer = IdentityManagementSerializer(data=dict_file)
        else:
            return Response(status = 400)
        system_all = System.objects.all()
        greater_version = 0
        for x in system_all:
            if(x.version > greater_version):
                greater_version = x.version
        serializer_system = SystemSerializer(data={"version": greater_version+1})
        if serializer.is_valid() and serializer_system.is_valid():
            serializer.save()
            serializer_system.save()
            return Response([serializer.data, serializer_system.data],status = 200)
        else:
            return Response([serializer.errors, serializer_system.errors],status = 400)

    def get(self, request, services, format = None):
        if services == 'get':
            system_all = System.objects.all()
            greater_version = 0
            for x in system_all:
                if(x.version > greater_version):
                    greater_version = x.version
            pdftoinvoice = PDFToInvoice.objects.latest('id')
            bi = BI.objects.latest('id')
            frontend = FrontEnd.objects.latest('id')
            management = IdentityManagement.objects.latest('id')

            filename = pdftoinvoice.file.name.split('/')[-1]
            response = HttpResponse(pdftoinvoice.file,content_type='application/zip', status = 200)
            response['Content-Disposition'] = 'attachment; filename=%s' % filename

            return response
        return Response(status = 400)
