from django.contrib import admin

# Register your models here.
from .models import Roles
from .models import Users

admin.site.register(Roles)
admin.site.register(Users)