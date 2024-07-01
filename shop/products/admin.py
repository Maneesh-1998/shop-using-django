from django.contrib import admin
from .models import product,offer

class productAdmin(admin.ModelAdmin):
   list_display=('name','price','stock')

class offerAdmin(admin.ModelAdmin):
   list_display=('code','discount')



admin.site.register(product,productAdmin)
admin.site.register(offer,offerAdmin)