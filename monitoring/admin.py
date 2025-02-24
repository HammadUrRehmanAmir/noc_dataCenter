from django.contrib import admin

# Register your models here.
from .models import NOC, Rack, Server

admin.site.register(NOC)
admin.site.register(Rack)
admin.site.register(Server)


