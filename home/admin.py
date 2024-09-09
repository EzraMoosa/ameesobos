"""
This module registers the models for the Django admin interface.

Models:
-------
- Song: Represents a song by the band.
- Member: Represents a band member and their details.
- Event: Represents an event where the band performs.

The registered models will be accessible and manageable via the Django admin
panel.
"""

# Libraries and modules
from django.contrib import admin
from .models import Song, Member, Event

# Register models for use in admin panel
admin.site.register(Song)
admin.site.register(Member)
admin.site.register(Event)
