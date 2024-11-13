from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('destinations/', views.destinations, name='destinations'),
    path('things_to_do/', views.things_to_do, name='things_to_do'),
    path('indian_calendar/', views.indian_calendar, name='indian_calendar'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('andhra_pradesh/', views.andhra_pradesh_detail, name='andhra_pradesh'),
    path('lakshadweep/', views.lakshadweep_detail, name='lakshadweep'),
    path('itinerary/', views.itinerary, name='itinerary'),
    path('state/<int:state_id>/', views.state_detail, name='state_detail'),
    path('login-signup/', views.login_signup, name='login_signup'),
]


