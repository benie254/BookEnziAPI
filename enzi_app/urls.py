from django.contrib import admin
from django.urls import path, include, re_path as url
from enzi_app import views 

urlpatterns = [
    url(r'^book/unit/$',views.ClientBookingView.as_view(),name='booking'),
    path('book/unit/confirm/<slug:uidb64>/<slug:token>/',views.activate,name='confirm-booking'),
    url(r'^payment/mpesa/$',views.payReq,name='pay-req'),
    url(r'^daraja/stk-push$', views.mpesa, name='mpesa'),
]