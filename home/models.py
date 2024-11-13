from django.db import models
from django.contrib.auth.models import User  # For handling users
from django.utils import timezone

# 1. Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# 2. Place Model (if needed for places separate from destinations)
class Place(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # Example: State, City, Food, Hotel
    description = models.TextField()
    image = models.ImageField(upload_to='places/')  # Assuming you want to upload images

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/')
    airfare = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Correctly defined
    food_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Changed from CharField to DecimalField
    hotel_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Changed from CharField to DecimalField
    description = models.TextField()

    def __str__(self):
        return self.name

# 4. Tour Package Model
class TourPackage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tour_packages')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    max_people = models.IntegerField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    available = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name='tour_packages')  # Link to categories

    def __str__(self):
        return f"{self.name} - {self.destination.name}"

# 5. Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_people = models.IntegerField()
    
    def is_upcoming(self):
        return self.start_date > timezone.now().date()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.tour_package.name}"

# 6. Review Model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - Rating: {self.rating}"

# 7. Things To Do Model (if needed)
class ThingsToDo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='things_to_do/')
    description = models.TextField()

    def __str__(self):
        return self.name

# 8. Plan Your Trip Model (if needed)
class PlanYourTrip(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='plan_your_trip/')
    description = models.TextField()

    def __str__(self):
        return self.name

# 9. Indian Calendar Model (if needed)
class IndianCalendar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='indian_calendar/')
    description = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='state_images/')

    def __str__(self):
        return self.name

class FunPlace(models.Model):
    state = models.ForeignKey(State, related_name='fun_places', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='fun_places_images/')

    def __str__(self):
        return self.name

class FamousFood(models.Model):
    state = models.ForeignKey(State, related_name='famous_foods', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='famous_foods_images/')

    def __str__(self):
        return self.name
    
    # models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username

# home/models.py
from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=50)  # The display name of the menu item
    url_name = models.CharField(max_length=50)  # The name of the URL pattern (e.g., 'login', 'signup')
    order = models.IntegerField(default=0)  # Field to specify the order of the items

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(self.url_name)
    
    class Meta:
        ordering = ['order']
