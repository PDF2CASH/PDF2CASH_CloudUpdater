from rest_framework import serializers
from .models import *

class SystemSerializer():
    class Meta:
        model = System
        fields = '__all__'

class PDFToInvoiceSerializer():
    class Meta:
        model = PDFToInvoice
        fields = '__all__'

class BISerializer():
    class Meta:
        model = BI
        fields = '__all__'

class IdentityManagementSerializer():
    class Meta:
        model = IdentityManagement
        fields = '__all__'

class FrontEndSerializer():
    class Meta:
        model = FrontEnd
        fields = '__all__'
