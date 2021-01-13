from django.contrib import admin

# Register your models here.

from rodzprod.models import Rodzaje,Produkty,Zaklady,Narzedzia,Surowce

admin.site.register(Rodzaje)
admin.site.register(Produkty)
admin.site.register(Zaklady)
admin.site.register(Surowce)
admin.site.register(Narzedzia)