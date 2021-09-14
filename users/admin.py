from users.models import User
from django.contrib import admin
from .models import *

# Register your models here.

class MembroAdmin(admin.ModelAdmin):
    list_display = ['usuario','id',]

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','id',]

class ConviteAdmin(admin.ModelAdmin):
    list_display = ['lider', 'planejamento', 'id',]

admin.site.register(User,UserAdmin)
admin.site.register(Membro, MembroAdmin)
admin.site.register(Convite, ConviteAdmin)