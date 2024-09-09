# Libraries and modules
from django.db import models


# Create your models here.
class Member(models.Model):

    """
    Represents a Member of the band.

    This model stores information about Members and Position.

    Attributes:
        name (CharField): This is the name or names of the member.
        position (Charfield): This is their role or position in the band.
        bio (TextField): This is a short bio of the member.
        image (ImageField): This is a photo or image of member.

    Methods:
        __str__: Returns a string representation of the member's name.
    """

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='members/')

    def __str__(self):
        
        """
        Return string representation of member's name.
        """

        return self.name


class Song(models.Model):
    
    """
    Represents a song from this band.

    This model stores information about Songs title, writers, release date and\
    lyrics

    Attributes:
        title (CharField): This is the name or title of the song.
        songwriter(s) (Charfield): The person or people who wrote this song.
        release_date (DateTimeField): The date the song was released.
        lyrics (TextField): Optional field for the lyrics of the song.

    Methods:
        __str__: Returns a string representation of the song's title.
    """

    title = models.CharField(max_length=200)
    songwriters = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    lyrics = models.TextField(blank=True, null=True)

    def __str__(self):

        """
        Return string representation of song title
        """

        return self.title
    

class Event(models.Model):
    
    """
    Represents an upcoming event from the band.

    This model stores information about event venue, city, country and date.

    Attributes:
        venue (CharField): This is the venue of the event.
        city (Charfield): The city where the event will take place.
        country (Charfield): The country where the event will take place.
        date (DateTimeField): The date of the upcoming event.

    Methods:
        __str__: Returns a string representation of the event's venue.
    """

    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):

        """
        Return string representation of event venue.
        """

        return self.venue
