from django.contrib import admin

# Register your models here.
from .models import Laptop, Desktop, Order, Feedback

admin.site.register(Laptop)
admin.site.register(Desktop)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)

admin.site.register(Order,OrderAdmin)
admin.site.register(Feedback)