from django.contrib import admin
from django.urls import path, include, re_path as url
from enzi_app import views 

urlpatterns = [
    path('',views.home,name='home'),
    url(r'^book/unit/$',views.ClientBookingView.as_view(),name='booking'),
    path('book/unit/confirm/<slug:uidb64>/<slug:token>/',views.activate,name='confirm-booking'),
]