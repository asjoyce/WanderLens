from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Destination, TourPackage, ThingsToDo, IndianCalendar, State
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.decorators import login_required

@login_required
def some_protected_view(request):
    # View code here
    pass

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

# home/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect('home')  # Redirect to home or any other page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_signup(request):
    return render(request, 'login_signup.html')

# Homepage view
def home(request):
    return render(request, 'home.html')

# Dashboard view
def dashboard(request):
    destinations = Destination.objects.all()
    tour_packages = TourPackage.objects.all()

    context = {
        'destinations': destinations,
        'tour_packages': tour_packages,
    }
    
    return render(request, 'dashboard.html', context)

def destinations(request):
    # Fetch all destinations (you might want to adjust this to filter based on user need)
    destinations = Destination.objects.all()
    context = {'destinations': destinations}
    return render(request, 'destinations.html', context)

from django.shortcuts import render

def things_to_do(request):
    months_data = {
        "January": {
            "places": ["Place 1", "Place 2", "Place 3"],
            "foods": ["Food 1", "Food 2", "Food 3"]
        },
        "February": {
            "places": ["Place 4", "Place 5", "Place 6"],
            "foods": ["Food 4", "Food 5", "Food 6"]
        },
        "March": {
            "places": ["Place 7", "Place 8", "Place 9"],
            "foods": ["Food 7", "Food 8", "Food 9"]
        },
        "April": {
            "places": ["Place 10", "Place 11", "Place 12"],
            "foods": ["Food 10", "Food 11", "Food 12"]
        },
        "May": {
            "places": ["Place 13", "Place 14", "Place 15"],
            "foods": ["Food 13", "Food 14", "Food 15"]
        },
        "June": {
            "places": ["Place 16", "Place 17", "Place 18"],
            "foods": ["Food 16", "Food 17", "Food 18"]
        },
        "July": {
            "places": ["Place 19", "Place 20", "Place 21"],
            "foods": ["Food 19", "Food 20", "Food 21"]
        },
        "August": {
            "places": ["Place 22", "Place 23", "Place 24"],
            "foods": ["Food 22", "Food 23", "Food 24"]
        },
        "September": {
            "places": ["Place 25", "Place 26", "Place 27"],
            "foods": ["Food 25", "Food 26", "Food 27"]
        },
        "October": {
            "places": ["Place 28", "Place 29", "Place 30"],
            "foods": ["Food 28", "Food 29", "Food 30"]
        },
        "November": {
            "places": ["Place 31", "Place 32", "Place 33"],
            "foods": ["Food 31", "Food 32", "Food 33"]
        },
        "December": {
            "places": ["Place 34", "Place 35", "Place 36"],
            "foods": ["Food 34", "Food 35", "Food 36"]
        },
    }
    return render(request, 'things_to_do.html', {'months_data': months_data})


def state_detail(request, state_id):
    state = get_object_or_404(State, id=state_id)
    fun_places = state.fun_places.all()
    famous_foods = state.famous_foods.all()
    return render(request, 'state_detail.html', {'state': state, 'fun_places': fun_places, 'famous_foods': famous_foods})

from datetime import datetime

def indian_calendar(request):
    return render(request, 'indian_calendar.html')


def filtered_destinations(request, category_name):
    # Fetch destinations that are linked to a specific category through TourPackage
    destinations = Destination.objects.filter(tour_packages__categories__name=category_name).distinct()
    context = {'destinations': destinations}
    return render(request, 'destinations.html', context)


# myapp/views.py

from django.shortcuts import render

def andhra_pradesh_detail(request):
    places = [
        {
            "name": "Visakhapatnam",
            "description": "A coastal city known for its beaches and the scenic Araku Valley.",
            "image": "https://media1.thrillophilia.com/filestore/bchw8n0ax74u07h3jplptwvf8q1x_1582274618_Araku_Valley.jpg?w=753&h=450&dpr=2.0",
            
        },
        {
            "name": "Tirupati",
            "description": "Famous for the Tirumala Venkateswara Temple, a significant pilgrimage site.",
            "image": "https://oneday.travel/wp-content/uploads/one-day-tirupati-local-temple-sightseeing-tour-package-private-cab-header.jpg",
            
        },
        {
            "name": "Visakhapatnam",
            "description": "A coastal city known for its beaches and the scenic Araku Valley.",
            "image": "https://media1.thrillophilia.com/filestore/bchw8n0ax74u07h3jplptwvf8q1x_1582274618_Araku_Valley.jpg?w=753&h=450&dpr=2.0",
            
        },
        {
            "name": "Tirupati",
            "description": "Famous for the Tirumala Venkateswara Temple, a significant pilgrimage site.",
            "image": "https://oneday.travel/wp-content/uploads/one-day-tirupati-local-temple-sightseeing-tour-package-private-cab-header.jpg",
            
        },
        {
            "name": "Visakhapatnam",
            "description": "A coastal city known for its beaches and the scenic Araku Valley.",
            "image": "https://media1.thrillophilia.com/filestore/bchw8n0ax74u07h3jplptwvf8q1x_1582274618_Araku_Valley.jpg?w=753&h=450&dpr=2.0",
            
        },
        {
            "name": "Tirupati",
            "description": "Famous for the Tirumala Venkateswara Temple, a significant pilgrimage site.",
            "image": "https://oneday.travel/wp-content/uploads/one-day-tirupati-local-temple-sightseeing-tour-package-private-cab-header.jpg",
            
        },
        {
            "name": "Visakhapatnam",
            "description": "A coastal city known for its beaches and the scenic Araku Valley.",
            "image": "https://media1.thrillophilia.com/filestore/bchw8n0ax74u07h3jplptwvf8q1x_1582274618_Araku_Valley.jpg?w=753&h=450&dpr=2.0",
            
        },
        {
            "name": "Tirupati",
            "description": "Famous for the Tirumala Venkateswara Temple, a significant pilgrimage site.",
            "image": "https://oneday.travel/wp-content/uploads/one-day-tirupati-local-temple-sightseeing-tour-package-private-cab-header.jpg",
            
        },
        {
            "name": "Visakhapatnam",
            "description": "A coastal city known for its beaches and the scenic Araku Valley.",
            "image": "https://media1.thrillophilia.com/filestore/bchw8n0ax74u07h3jplptwvf8q1x_1582274618_Araku_Valley.jpg?w=753&h=450&dpr=2.0",
            
        },
        {
            "name": "Tirupati",
            "description": "Famous for the Tirumala Venkateswara Temple, a significant pilgrimage site.",
            "image": "https://oneday.travel/wp-content/uploads/one-day-tirupati-local-temple-sightseeing-tour-package-private-cab-header.jpg",
            
        },
        # Add more places as needed
    ]
    return render(request, 'lakshadweep_detail.html', {'places': places})


def itinerary(request):
    return render(request, 'itinerary.html')


from django.shortcuts import render
from .models import Place
from .forms import TripPlanForm

def lakshadweep_detail(request):
    places = [
        {
            "name": "Agatti Island",
            "description": "Known for its beautiful coral reefs and clear blue waters, perfect for snorkeling and scuba diving.",
            "image": "https://example.com/agatti_island.jpg",
        },
        {
            "name": "Bangaram Island",
            "description": "A secluded paradise ideal for water sports, featuring white sandy beaches and crystal-clear lagoons.",
            "image": "https://example.com/bangaram_island.jpg",
        },
        {
            "name": "Minicoy Island",
            "description": "Famous for its distinct culture, lighthouse, and rich marine life, making it a unique destination.",
            "image": "https://example.com/minicoy_island.jpg",
        },
        # Add more places if needed
    ]
    
    if request.method == "POST":
        form = TripPlanForm(request.POST)
        if form.is_valid():
            budget = form.cleaned_data['budget']
            days = form.cleaned_data['days']
            people = form.cleaned_data['people']

            suggestions = generate_suggestions(budget, days, people)
            return render(request, 'lakshadweep_detail.html', {'places': places, 'form': form, 'suggestions': suggestions})
    else:
        form = TripPlanForm()

    return render(request, 'lakshadweep_detail.html', {'places': places, 'form': form})

def generate_suggestions(budget, days, people):
    # Simple suggestion logic (modify as needed)
    daily_budget = budget / days
    suggestions = []
    for day in range(1, days + 1):
        activity = f"Day {day}: Enjoy activities worth around {daily_budget / people:.2f} per person."
        suggestions.append(activity)
    return suggestions


