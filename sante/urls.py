from django.urls import path
from . import views


urlpatterns = [
    path('', views.registerCustomer, name='register-client'),
    path('login-client/', views.loginCustomer, name='login-client'),
    path('login-out/', views.logOutUser, name='logout-client'),
    path("home/", views.dashCleint, name="dash-client"),
    path("hospi/", views.dashHospi, name="dash-hospital"),
    path("pharmaci/", views.dashPharmaci, name="dash-pharmaci")
]