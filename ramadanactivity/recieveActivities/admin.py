from django.contrib import admin

from .models import Activity, ActivityParticipant

# Register your models here.
admin.site.register(Activity)
admin.site.register(ActivityParticipant)