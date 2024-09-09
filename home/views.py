# Libraries and models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Song, Member, Event


@login_required
def homepage(request):

    """
    Render home page of band.

    Displays the homepage with the navbar visible.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponse
        The rendered homepage with the navbar included.
    """

    return render(request, 'home/home.html', {'show_navbar': True})


@login_required
def members_list(request):

    """
    Display a list of all current members of the band.

    Retrieves all members from the database and renders members list page.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponse
        The rendered members list page with all members.
    """

    members = Member.objects.all()
    return render(request, 'home/members.html', {'members': members,
                                                 'show_navbar': True})


@login_required
def songs_list(request):

    """
    Display the list of all songs by the band.

    Retrieves all songs from database and renders the songs list page.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponse
        The rendered songs list page with the list of all songs.
    """

    songs = Song.objects.all()
    return render(request, 'home/songs.html', {'songs': songs,
                                               'show_navbar': True})


@login_required
def song_detail(request, pk):

    """
    Display details of a single song.

    Retrieves the song with the given primary key (pk) from the database and
    renders the song detail page.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.
    pk : int
        The primary key of the song to be retrieved.

    Returns:
    --------
    HttpResponse
        The rendered song detail page with the details of the song.
    """

    song = get_object_or_404(Song, pk=pk)
    return render(request, 'home/detail.html', {'song': song,
                                                'show_navbar': True})


@login_required
def events_list(request):

    """
    Display the list of upcoming events of the band.

    Retrieves all upcoming events from the database and renders the events list
    page.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponse
        The rendered events list page with the list of upcoming events.
    """

    events = Event.objects.all()
    return render(request, 'home/events.html', {'events': events,
                                                'show_navbar': True})
