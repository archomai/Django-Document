from django.contrib import admin

from inheritance.multi_table.models import Place, Restaurant

admin.site.register(Place)
admin.site.register(Restaurant)
