from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import HttpResponse
import zipfile


class SystemView(APIView):

    def post(self, request, services, format=None):
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
        if services == 'zip':
            pdftoinvoice = PDFToInvoice.objects.latest('id')
            bi = BI.objects.latest('id')
            frontend = FrontEnd.objects.latest('id')
            management = IdentityManagement.objects.latest('id')
            pdftoinvoice_content = pdftoinvoice.file.read()
            bi_content = bi.file.read()
            frontend_content = frontend.file.read()
            management_content = management.file.read()
            zip = zipfile.ZipFile('system.zip','w')
            zip.write(pdftoinvoice.file.name)
            zip.write(bi.file.name)
            zip.write(frontend.file.name)
            zip.write(management.file.name)
            zip.close()
            zip = open('system.zip', 'rb')
            filename = 'system.zip'
            response = HttpResponse(zip,content_type='application/zip', status=200)
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            return response
        if services == 'version':
            system_all = System.objects.all()
            greater_version = 0
            for x in system_all:
                if(x.version > greater_version):
                    greater_version = x.version
            return Response({'version':greater_version}, status=200)
        return Response(status=400)
