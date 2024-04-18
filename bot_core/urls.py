from django.urls import path
from . import views



urlpatterns = [

    path('bot_status/', views.bot_status_view, name='bot_status'),
]


