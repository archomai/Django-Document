from django.contrib import admin

from one_to_one.models import (
    Place, Restaurant, Waiter
)

admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
