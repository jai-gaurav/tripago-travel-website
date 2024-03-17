from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, ItineraryGenerationForm, TripGenerationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from . prompt import createTripPrompt, createItineraryPrompt, getHermesAIResponse

# authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, 'tripago/index.html')


def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form = CreateUserForm(data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        if form.is_valid():
            form.save()

            return redirect('login')

    return render(request, 'tripago/register.html')


def login(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        form = LoginForm(request, data={
            'username': username,
            'password': password
        
        })

        if form.is_valid():
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    return render(request, 'tripago/login.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'tripago/dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect("")


def create_itinerary(request):
    form = ItineraryGenerationForm()

    if request.method == "POST":
        start_location = request.POST.get('start_location')
        destination = request.POST.get('destination')
        budget = request.POST.get('budget')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        group_size = request.POST.get('group_size')
        mode_of_arrival = request.POST.get('mode_of_arrival')
        mode_of_transport = request.POST.get('mode_of_transport')
        accommodation = request.POST.get('accommodation')
        activities = request.POST.get('activities')
        extra_info = request.POST.get('extra_info')

        data = {
            'start_location': start_location,
            'destination': destination,
            'budget': budget,
            'start_date': start_date,
            'end_date': end_date,
            'group_size': group_size,
            'mode_of_arrival': mode_of_arrival,
            'mode_of_transport': mode_of_transport,
            'accommodation': accommodation,
            'activities': ", ".join(activities.split('\r\n')),
            'extra_info': extra_info
        }

        form = ItineraryGenerationForm(data=data)

        if form.is_valid():
            prompt = createItineraryPrompt(data)
            with open('tripago/itinerary_prompt.txt', 'w') as f:
                f.write(prompt)
            return HttpResponse("Itinerary Created")
        
        return HttpResponse("Invalid Form")

    return render(request, 'tripago/create-itinerary.html')

def create_trip(request):
    form = TripGenerationForm()

    if request.method == "POST":
        start_location = request.POST.get('start_location')
        destination = request.POST.get('destination')
        budget = request.POST.get('budget')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        mode_of_arrival = request.POST.get('mode_of_arrival')
        stay_preference = request.POST.get('stay_preference')
        activity_preference = request.POST.get('activity_preference')
        group_size = request.POST.get('group_size')
        mode_of_transport = request.POST.get('mode_of_transport')

        data = {
            'start_location': start_location,
            'destination': destination,
            'budget': budget,
            'start_date': start_date,
            'end_date': end_date,
            'mode_of_arrival': mode_of_arrival,
            'stay_preference': stay_preference,
            'activity_preference': activity_preference,
            'group_size': group_size,
            'mode_of_transport': mode_of_transport
        }

        form = TripGenerationForm(data=data)

        if form.is_valid():
            prompt = createTripPrompt(data)
            with open('tripago/trip_prompt.txt', 'w') as f:
                f.write(prompt)
            return HttpResponse("Trip Created")


    context = {'tripgenerationform': form}

    return render(request, 'tripago/create-trip.html', context=context)


def hermes_ai(request):
    if request.method == "POST":
        prompt = request.POST.get('chat-prompt')
        answer = getHermesAIResponse(prompt)
        return JsonResponse({'answer': answer})

    return render(request, 'tripago/hermes-ai.html')


def france(request):
    return render(request, 'tripago/france.html')

def spain(request):
    return render(request, 'tripago/spain.html')

def usa(request):
    return render(request, 'tripago/usa.html')

def switzerland(request):
    return render(request, 'tripago/switzerland.html')

def thailand(request):
    return render(request, 'tripago/thailand.html')