# Libraries and models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Song, Member, Event


@login_required
def homepage(request):

    """
    Render home page of band. Show navbar.
    """

    return render(request, 'home/home.html', {'show_navbar' : True})


@login_required
def members_list(request):

    """
    Get and display positions of the current members of the band. Show navbar.
    """

    members = Member.objects.all()
    return render(request, 'home/members.html', {'members' : members, \
                                                 'show_navbar' : True})


@login_required
def songs_list(request):
    
    """
    Get and display links to all songs of the band. Show navbar.
    """

    songs = Song.objects.all()
    return render(request, 'home/songs.html', {'songs' : songs, \
                                               'show_navbar' : True})


@login_required
def song_detail(request, pk):
    
    """
    Get single song detail. Show navbar.
    """

    song = get_object_or_404(Song, pk=pk)
    return render(request, 'home/detail.html', {'song' : song, \
                                                'show_navbar' : True})


@login_required
def events_list(request):
    
    """
    Get and display all upcoming events of the band. Show navbar.
    """

    events = Event.objects.all()
    return render(request, 'home/events.html', {'events' : events, \
                                                'show_navbar' : True})
