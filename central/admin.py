from django.contrib import admin

# Register your models here.

from central.models import JogadorTest, Utilizador

class JogadorTestt(admin.ModelAdmin):
    list_display = (id, 'name', 'phone', 'code', 'equipa')
    list_display_links = (id, 'name')
    search_fields = ('name', 'code')

class Utilizadort(admin.ModelAdmin):
    list_display = (id, 'name', 'phone', 'email', 'senha')
    list_display_links = (id, 'name')
    search_fields = ('name', 'email')


admin.site.register(Utilizador, Utilizadort)

admin.site.register(JogadorTest, JogadorTestt)
