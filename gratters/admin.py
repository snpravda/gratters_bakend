from django.contrib import admin
from .models import *

# Register your models here.

class GratterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Gratter, GratterAdmin)
