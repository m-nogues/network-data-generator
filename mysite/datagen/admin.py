from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Action)
admin.site.register(Attack)
admin.site.register(Behavior)
admin.site.register(Bias)
admin.site.register(Command)
admin.site.register(Experiment)
admin.site.register(Hacker)
admin.site.register(Parameter)
admin.site.register(Service)
admin.site.register(Vm)
