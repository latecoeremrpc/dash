from django.urls import path, include
from order_past import views
urlpatterns = [
    path('home/',views.home,name='order_past_home'),
]