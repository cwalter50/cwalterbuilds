from django.shortcuts import render
# from ordersorter.models import User
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
# from django.contrib.auth.decorators import login_required, user_passes_test

# from .models import User, Listing, Bid, Comment
# from .forms import CommentForm, ListingForm, BidForm

# Create your views here.
def index(request):
    
    return render(request, "myprojects/index.html", {

    })

def myprojects(request):
    return render(request, "myprojects/myprojects.html", {

    })


# HTTP Error 404
def error_404(request, exception):
    data = {
        'errorNum': '404',
        'errorDirections': 'The page you are looking for was not found.',
    }
    return render(request,'ordersorter/error.html', data)

def error_500(request):
    data = {
        'errorNum': '500',
        'errorTitle': 'Opps! Internal Server Error!',
        'errorDirections': 'Unfortunately we\'re having trouble loading the page you are looking for. Please come back in a while.'
    }
        
    return render(request,'ordersorter/error.html', data)

def error_400(request, exception):
    data = {
        'errorNum': '400',
        'errorTitle': 'Opps! Bad Request',
        'errorDirections': 'The server cannot process the request due to something that is perceived to be a client error.'
    }
        
    return render(request,'ordersorter/error.html', data)

def error_403(request, exception):
    data = {
        'errorNum': '403',
        'errorTitle': 'Opps! Forbidden',
        'errorDirections': 'Unfortunately the page you are trying to reach is forbidden'
    }
        
    return render(request,'ordersorter/error.html', data)


# Login, Register, and Logout....

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("myprojects:index"))
        else:
            return render(request, "myprojects/registration/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "myprojects/registration/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("myprojects:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "myprojects/registration/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "myprojects/registration/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("myprojects:index"))
    else:
        return render(request, "myprojects/registration/register.html")
