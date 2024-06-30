from django.contrib import admin
from .models import ServiceUser, Services, Subscription
# Register your models here.

admin.site.register(ServiceUser)
admin.site.register(Services)
admin.site.register(Subscription)

