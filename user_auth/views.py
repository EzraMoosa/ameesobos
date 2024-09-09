# Libraries and modules
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def authenticate_user(request):

    """
    Authenticate the user's login credentials and log in if valid.

    This view processes POST requests containing username and password,
    attempts to authenticate user and logs them in if credentials are correct.
    If authentication fails, the user is redirected back to login page with an
    error message.

    Args:
    -----
        request (HttpRequest): The HTTP request object containing the user's
        credentials.

    Returns:
    --------
        HttpResponseRedirect: Redirects to the login page if authentication
        fails or to the homepage if successful.
    """

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
    Renders the login page.

    This view function renders the login page where users can input their 
    credentials to login.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponse
        A response object containing the rendered login page template.
    """

    return render(request, 'authentication/login.html', {'show_navbar': False})


@login_required
def user_logout(request):

    """
    Logs user out and redirects to the login page.

    This view function logs the current user out of the system and redirects
    them to the login page.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponseRedirect
        A redirect response to the login page.
    """

    logout(request)
    return HttpResponseRedirect(reverse('user_auth:login'))


def register(request):

    """
    Registers a new user with a username, first name and password.

    This view handles user registration. It checks if username already exists
    and if password match. After successful registration the user is redirected
    to the login page.

    Parameters:
    -----------
    request : HttpRequest
        The HTTP request object.

    Returns:
    --------
    HttpResponseRedirect
        Redirects to the registration page if there's an error or login page
        if successful.
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
        User.objects.create_user(username=username, password=password1,
                                 first_name=first_name)
        messages.success(request, 'User registered successfully.')
        return HttpResponseRedirect(reverse('user_auth:login'))

    return render(request, 'authentication/register.html',
                  {'show_navbar': False})


# References & Resources:
# 1. https://forum.djangoproject.com/t/refreshing-the-page-resubmits-the-django-form/11362
# 2. https://forum.djangoproject.com/t/user-first-name/10249
# 3. https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/
# 4. https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django
# 5. https://docs.djangoproject.com/en/5.0/topics/auth/
