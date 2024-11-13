from django.contrib import admin
from .models import (
    Category,
    Destination,
    TourPackage,
    Booking,
    Review,
    ThingsToDo,  # Ensure you have the correct model name here
    PlanYourTrip,
    IndianCalendar,
    State, 
    FunPlace, 
    FamousFood,
    MenuItem
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(TourPackage)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(ThingsToDo)  # Use the correct model name
admin.site.register(PlanYourTrip)
admin.site.register(IndianCalendar)
admin.site.register(State)
admin.site.register(FunPlace)
admin.site.register(FamousFood)
# admin.py
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Optionally, if you want to customize the User Admin view
class CustomUserAdmin(UserAdmin):
    # You can customize the admin interface here if needed
    pass

admin.site.unregister(User)  # Unregister the default User model
admin.site.register(User, CustomUserAdmin)  # Register the customized User model

# home/admin.py

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_name', 'order')
    ordering = ('order',)
