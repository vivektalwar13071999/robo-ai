from django.contrib import admin
from .models import general, robotics, embedded, machine, imagepro

# Register your models here.
admin.site.register(general)
admin.site.register(robotics)
admin.site.register(embedded)
admin.site.register(machine)
admin.site.register(imagepro)