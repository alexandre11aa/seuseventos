from django.urls import path
from main import views

urlpatterns = [

    # Public pages

    path('home/', views.homepage, name='home'),
    path('events/', views.eventspage, name = 'events'),
    path('event_details/<int:event_id>/', views.event_details_page, name = 'event_details'),

    # Individual pages

    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutpage, name = 'logout'),
    path('profile/', views.profilepage, name = 'profile'),
    path('create/', views.createpage, name = 'create'),
    path('edit_profile/', views.edit_profile_page, name = 'edit_profile'),
    path('edit_event/<int:event_id>/', views.edit_event_page, name = 'edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event_page, name='delete_event'),
]