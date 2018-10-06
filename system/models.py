from django.db import models


class System(models.Model):
    version = models.IntegerField()

class PDFToInvoice(models.Model):
    files = models.FileField(upload_to='documents/PDFToInvoice/')

class IdentityManagement(models.Model):
    files = models.FileField(upload_to='documents/IdentityManagement/')

class BI(models.Model):
    files = models.FileField(upload_to='documents/BI/')

class FrontEnd(models.Model):
    files = models.FileField(upload_to='documents/FrontEnd/')
