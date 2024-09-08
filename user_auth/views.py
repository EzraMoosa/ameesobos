# Libraries and modules
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def authenticate_user(request):
    """Authenticate user's login information."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if user exists or not
        if user is None:
            messages.error(request, 'Invalid username or password, try again.')
            return HttpResponseRedirect(reverse('user_auth:login'))
        else:
            # Sign user in
            login(request, user)
            return HttpResponseRedirect(reverse('home:homepage'))
    
    # Redirect to login page
    return HttpResponseRedirect(reverse('user_auth:login'))


def user_login(request):

    """
    Return login page.
    """

    return render(request, 'authentication/login.html', {'show_navbar': False})


@login_required
def user_logout(request):

    """
    Log user out. Redirect to login page.
    """

    logout(request)
    return HttpResponseRedirect(reverse('user_auth:login'))


def register(request):

    """
    Register new user's Username, First Name and Password.
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return HttpResponseRedirect(reverse('user_auth:register'))
        
        # Validate if passwords match
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return HttpResponseRedirect(reverse('user_auth:register'))
        
        # Create the user if no errors
        User.objects.create_user(username=username, password=password1, \
                                  first_name=first_name)
        messages.success(request, 'User registered successfully.')
        return HttpResponseRedirect(reverse('user_auth:login'))
    
    return render(request, 'authentication/register.html', \
                  {'show_navbar': False})


# References & Resources:
# 1. https://forum.djangoproject.com/t/refreshing-the-page-resubmits-the-django-form/11362
# 2. https://forum.djangoproject.com/t/user-first-name/10249
# 3. https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/
# 4. https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
# 5. https://docs.djangoproject.com/en/5.0/topics/auth/
