from django.urls import path

from . import views

app_name = 'asovi_app'
urlpatterns = [
    path('profile_edit/',views.profile_edit,name='profile-edit'),
]