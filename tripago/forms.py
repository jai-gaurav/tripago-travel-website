from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username', 
                  'email',
                  'password1', 
                  'password2'
                  ]
        
# authenticate a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# create an itinerary
class ItineraryGenerationForm(forms.Form):
    start_location = forms.CharField(widget=TextInput())
    destination = forms.CharField(widget=TextInput())
    budget = forms.DecimalField(max_digits=10, decimal_places=2)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    group_size = forms.IntegerField()
    mode_of_arrival = forms.CharField(widget=TextInput())
    mode_of_transport = forms.CharField(widget=TextInput())
    accommodation = forms.CharField(widget=TextInput())
    activities = forms.CharField(widget=forms.Textarea())
    extra_info = forms.CharField(widget=forms.Textarea())

# create a trip
class TripGenerationForm(forms.Form):
    start_location = forms.CharField(widget=TextInput())
    destination = forms.CharField(widget=TextInput())
    budget = forms.DecimalField(max_digits=10, decimal_places=2)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # how to reach destination
    mode_of_arrival = forms.ChoiceField(widget=forms.Select, choices=[('Flight', 'Flight'), 
                                                                      ('Train', 'Train'), 
                                                                      ('Bus', 'Bus'), 
                                                                      ('Car', 'Car'), 
                                                                      ('Boat', 'Boat'), 
                                                                      ('Other', 'Other')])
    
    stay_preference = forms.ChoiceField(widget=forms.Select, choices=[('Hotel', 'Hotel'),
                                                                      ('Hostel', 'Hostel'),
                                                                      ('Airbnb', 'Airbnb'),
                                                                      ('Other', 'Other')])
    
    activity_preference = forms.ChoiceField(widget=forms.Select, choices=[('Sightseeing', 'Sightseeing'),
                                                                          ('Adventure', 'Adventure'),
                                                                          ('Relaxation', 'Relaxation'),
                                                                          ('Business', 'Business'),
                                                                          ('Other', 'Other')])
    group_size = forms.IntegerField()
    
    # how to travel at destination
    mode_of_transport = forms.ChoiceField(widget=forms.Select, choices=[('Flight', 'Flight'),
                                                                        ('Train', 'Train'),
                                                                        ('Bus', 'Bus'),
                                                                        ('Car', 'Car'),
                                                                        ('Boat', 'Boat'),
                                                                        ('Bike', 'Bike'),
                                                                        ('Walk', 'Walk'),
                                                                        ('Other', 'Other')])
