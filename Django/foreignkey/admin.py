from django.contrib import admin

from foreignkey.models import Manufacturer, Car, Person

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Person)
