from django.contrib import admin

# Register your models here.

from central.models import AlunoTest

class AlunoTestt(admin.ModelAdmin):
    list_display = (id, 'name', 'phone', 'code')
    list_display_links = (id, 'name')
    search_fields = ('name', 'code')

admin.site.register(AlunoTest, AlunoTestt)
