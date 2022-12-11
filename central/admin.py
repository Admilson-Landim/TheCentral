from django.contrib import admin

# Register your models here.

from central.models import JogadorTest

class JogadorTestt(admin.ModelAdmin):
    list_display = (id, 'name', 'phone', 'code', 'equipa')
    list_display_links = (id, 'name')
    search_fields = ('name', 'code')

admin.site.register(JogadorTest, JogadorTestt)
