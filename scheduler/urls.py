from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('api/booked-days/', views.get_booked_days, name='get_booked_days'),
    path('api/book/', views.book_order, name='book_order'),
]
