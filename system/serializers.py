from rest_framework import serializers
from .models import (
    PDFToInvoice,
    BI,
    FrontEnd,
    APIGateway,
    System,
    Parser,
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


class APIGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIGateway
        fields = '__all__'


class FrontEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontEnd
        fields = '__all__'


class ParserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parser
        fields = '__all__'
