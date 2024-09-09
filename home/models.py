# Libraries and modules
from django.db import models


# Create your models here.
class Member(models.Model):

    """
    Represents a Member of the band.

    This model stores information about Members and Position.

    Attributes:
    -----------
        name : models.CharField
            The name of the member.
        position : models.CharField
            The member's role or position in the band.
        image : models.ImageField
            A photo or image of the member.


    Methods:
    --------
        __str__():
            Returns a string representation of the member's name.
    """

    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='members/')

    def __str__(self):

        """
        Returns:
        --------
        str
            A string representation of member's name.
        """

        return self.name


class Song(models.Model):

    """
    Represents a song from this band.

    This model stores information about Songs title, writers, release date and\
    lyrics

    Attributes:
    -----------
        title : models.CharField
            The title of the songs.
        songwriters : models.CharField
            The person(s) who wrote the song.
        release_date : models.DateTimeField
            The date the song was released.
        lyrics : models.TextField
            The lyrics of the song.

    Methods:
    --------
        __str__():
            Returns a string representation of the song's title.
    """

    title = models.CharField(max_length=200)
    songwriters = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    lyrics = models.TextField(blank=True, null=True)

    def __str__(self):

        """
        Returns:
        --------
        str
            A string representation of song title.
        """

        return self.title


class Event(models.Model):

    """
    Represents an upcoming event from the band.

    This model stores information about event venue, city, country and date.

    Attributes:
    -----------
        venue : models.CharField
            The venue where the event will take place.
        city : models.CharField
            The city where the event will take place.
        country : models.CharField
            The country where the event will take place.
        date : models.DateTimeField
            The date of the event.

    Methods:
    --------
        __str__():
            Returns a string representation of the event's venue.
    """

    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):

        """
        Returns:
        --------
        str
            A string representation of event venue.
        """

        return self.venue
