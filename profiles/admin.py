from django.contrib import admin

from profiles.models import Planet, Jedi, Padawan, Order

admin.site.register(Planet)
admin.site.register(Order)
admin.site.register(Jedi)
admin.site.register(Padawan)
