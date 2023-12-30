from django.urls import path
from . import views

urlpatterns = [
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]