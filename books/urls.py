from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),

]


