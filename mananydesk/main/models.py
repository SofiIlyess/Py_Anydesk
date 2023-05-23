from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import FileExtensionValidator
from .validators import validate_file

class Client(models.Model):
    name = models.CharField(max_length=150)
    anydesk = models.CharField(max_length=12)
    session = models.CharField(max_length=150,default="None")
    anypwd = models.CharField(max_length=150)
    winpwd = models.CharField(max_length=150)
    tel = models.CharField(max_length=50,blank=True,null=True)
    tel2 = models.CharField(max_length=50,blank=True,null=True)
    note = models.TextField(blank=True,null=True)
    createdon = models.DateTimeField(default=datetime.datetime.now())
    updatedon = models.DateTimeField(blank=True,null=True)
    createdby = models.ForeignKey(User,on_delete=models.CASCADE)
    updatedby = models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name
    
class ClientsImport(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    imported = models.BooleanField(default=False)
    file = models.FileField(upload_to='Clients/',validators=[validate_file])

    def __str__(self) -> str:
        return self.owner.username