from django.db import models


class System(models.Model):
    version = models.IntegerField(unique=True)


class PDFToInvoice(models.Model):
    file = models.FileField(upload_to='system/documents/PDFToInvoice/')


class APIGateway(models.Model):
    file = models.FileField(upload_to='system/documents/APIGateway/')


class BI(models.Model):
    file = models.FileField(upload_to='system/documents/BI/')


class FrontEnd(models.Model):
    file = models.FileField(upload_to='system/documents/FrontEnd/')


class Parser(models.Model):
    file = models.FileField(upload_to='system/documents/Parser/')
