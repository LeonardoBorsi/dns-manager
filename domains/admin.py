from django.contrib import admin

from .models import (TLD, Domain, SubDomain)

admin.site.register(TLD)
admin.site.register(Domain)
admin.site.register(SubDomain)

