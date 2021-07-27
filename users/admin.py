from users.models import User
from django.contrib import admin
from .models import *

# Register your models here.

class MembroAdmin(admin.ModelAdmin):
    list_display = ['usuario','lider_elemento','id',]

admin.site.register(User)
admin.site.register(Membro, MembroAdmin)