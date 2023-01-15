from django.contrib import admin

from .models import material, Herramientas, LaborIndirecta, Factura

# Register your models here.

admin.site.register(material)
admin.site.register(Herramientas)
admin.site.register(LaborIndirecta)
admin.site.register(Factura)


