from django.contrib import admin

# Register your models here.
from west.models import Character, Contact, Tag, ContactAdmin

admin.site.register([Character, Tag])
admin.site.register(Contact, ContactAdmin)
