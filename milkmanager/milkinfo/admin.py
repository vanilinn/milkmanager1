from django.contrib import admin
from .models import Cistern


class CisternAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume', 'current_volume')  # Определите, какие поля отображать в списке объектов модели


admin.site.register(Cistern, CisternAdmin)
