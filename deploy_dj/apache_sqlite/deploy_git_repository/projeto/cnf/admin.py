from django.contrib import admin
from .models import Porta

# class PortaAdmin(admin.ModelAdmin):
#     fields = (
#                 'id', 
#                 'modelo', 
#                 'andar', 
#                 'porta_1', 
#                 'porta_2', 
#                 'observacao',
#                 'data_publicacao',
#                 'autor',
#                 )

admin.site.register(Porta)