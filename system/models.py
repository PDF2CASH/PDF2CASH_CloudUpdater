from django.db import models


class System(models.Model):
    version = models.IntegerField(unique=True)


class PDFToInvoice(models.Model):
    file = models.FileField(upload_to='system/documents/PDFToInvoice/')


class IdentityManagement(models.Model):
    file = models.FileField(upload_to='system/documents/IdentityManagement/')


class BI(models.Model):
    file = models.FileField(upload_to='system/documents/BI/')


class FrontEnd(models.Model):
    file = models.FileField(upload_to='system/documents/FrontEnd/')
