
#Libraries and modules
from django.contrib import admin
from .models import Song, Member, Event


# Register models for use in admin panel
admin.site.register(Song)
admin.site.register(Member)
admin.site.register(Event)
