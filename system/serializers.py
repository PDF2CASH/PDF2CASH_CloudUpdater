from rest_framework import serializers
from .models import (
    PDFToInvoice,
    BI,
    FrontEnd,
    IdentityManagement,
    System
)


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'


class PDFToInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFToInvoice
        fields = '__all__'


class BISerializer(serializers.ModelSerializer):
    class Meta:
        model = BI
        fields = '__all__'


class IdentityManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityManagement
        fields = '__all__'


class FrontEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontEnd
        fields = '__all__'
