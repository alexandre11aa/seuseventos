from main.models import *

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import *

from .models import *

def homepage(request):

    return render(request, template_name='home.html')

def registerpage(request):

    if request.user.is_authenticated:
        return render(request, template_name='profile.html')
    
    else:
        if request.method == 'GET':
            return render(request, template_name='register.html')
        
        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            if User.objects.filter(username=username).exists():

                return redirect('register')
            
            else:

                user = User.objects.create_user(username=username, password=password, email=email)

                login(request, user)

                return redirect('home') 

def loginpage(request):

    if request.user.is_authenticated:
        return render(request, template_name='profile.html')
    
    else:
        if request.method == 'GET':
            return render(request, template_name='login.html')
        
        if request.method == 'POST':
            username = request.POST.get('username1')
            password = request.POST.get('password1')

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                
                return redirect('profile')
            
            else:
                return redirect('login')
            
def logoutpage(request):
    
    logout(request)

    return redirect('home')

def profilepage(request):

    if request.user.is_authenticated:
        if request.user.is_authenticated:
            user_info = {
                'username': request.user.username,
                'email': request.user.email,
            }

        items = event.objects.filter(user=request.user) 

        return render(request, 'profile.html', {'user_info': user_info, 'items': items})
    
    else:
        return redirect('login')

def createpage(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, template_name='create.html')
        
        if request.method == 'POST':

            user = request.user 

            name = request.POST.get('name')
            banner = request.FILES.get('banner')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            adress = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            date = request.POST.get('eventDate')
            start_time = request.POST.get('eventTimeStart')
            end_time = request.POST.get('eventTimeEnd')
            description = request.POST.get('description')

            event.objects.create(
                user=user,
                name = name,
                banner = banner,
                email = email,
                phone = phone,
                adress = adress,
                city = city,
                state = state,
                country = country,
                date = date,
                start_time = start_time,
                end_time = end_time,
                description = description
            )

            return redirect('events')
    
    else:
        return redirect('login')
    
def eventspage(request):

    items = event.objects.all()

    return render(request, template_name='events.html', context={'items': items})

def event_details_page(request, event_id):

    item = get_object_or_404(event, id=event_id)

    if request.method == 'POST':
        form = ParticipantForm(request.POST)

        if form.is_valid():
            participants = form.save(commit=False)
            participants.events = item
            participants.save()

            return redirect('event_details', event_id=event_id)
        
    else:
        participants_list = participant.objects.filter(events=item)

        return render(request, 'event_details.html', {'item': item, 'participants_list': participants_list})

def edit_profile_page(request):

    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, template_name='edit_profile.html')
        
        if request.method == 'POST':

            form = EditProfileForm(request.POST or None, instance=request.user)

            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')

                if password:
                    user.set_password(password)

                user.save()

                return redirect('profile')
    
            else:
                return redirect('edit_profile')
    
    else:
        return redirect('login')

def edit_event_page(request, event_id):

    if request.user.is_authenticated:

        event_instance = event.objects.get(id=event_id)

        event_form = EditEventForm(request.POST, request.FILES, instance=event_instance)

        if request.method == 'GET':
            return render(request, 'edit_event.html', {'event_instance': event_instance})
        
        if request.method == 'POST':

            if event_form.is_valid():
                edited_event = event_form.save(commit=False)
                edited_event.save()

                return redirect('profile')

            else:
                return redirect('edit_event')
    
    else:
        return redirect('login')
    
def delete_event_page(request, event_id):

    event_delete = event.objects.get(id=event_id, user=request.user)

    event_delete.delete()

    return redirect('profile')