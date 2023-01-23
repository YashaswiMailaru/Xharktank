
from django.urls import path
from django.urls import re_path
from myapi import views


urlpatterns = [
    path('pitches/', views.pitch_list),
    path('pitches/<int:pk>/', views.pitch_detail),
    path('pitches/<int:pk>/makeOffer/', views.make_offer),
    path('pitches', views.pitch_list),
    path('pitches/<int:pk>', views.pitch_detail),
    path('pitches/<int:pk>/makeOffer', views.make_offer),
]
