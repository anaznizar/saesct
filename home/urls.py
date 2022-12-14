
from django.urls import path
  
# importing views from views..py
from .views import home,about,events,archive
  
urlpatterns = [
    path('', home ),
    path('about', about ),
    path('events', events ),
    path('archive', archive ),
]