
from django.contrib import admin
from django.apps import apps


myapp = apps.get_app_config('ticketing')
admin.site.register(myapp.get_models())
