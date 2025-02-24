from django.db import models

# Create your models here.
class NOC(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Rack(models.Model):
    noc = models.ForeignKey(NOC, on_delete=models.CASCADE)
    rack_number = models.IntegerField()

    def __str__(self):
        return f"Rack {self.rack_number} in {self.noc.name}"


class Server(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    server_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    
    def __str__(self):
        return self.server_name

   
