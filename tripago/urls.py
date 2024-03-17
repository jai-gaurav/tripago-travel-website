from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('register.html', views.register, name="register"),
    path('login.html', views.login, name="login"),
    path('dashboard.html', views.dashboard, name="dashboard"),
    path('logout.html', views.logout, name="logout"),
    path('france.html', views.france, name="france"),
    path('spain.html', views.spain, name='spain'),
    path('usa.html', views.usa, name="usa"),
    path('switzerland.html', views.switzerland, name="switzerland"),
    path('thailand.html', views.thailand, name="thailand"),
    path('create-itinerary.html', views.create_itinerary, name="create-itinerary"),
    path('create-trip.html', views.create_trip, name="create-trip"),
    path('hermes-ai.html', views.hermes_ai, name="hermes-ai"),
]