from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('notes/', views.note_list, name='note_list'),

    path('add/', views.add_note, name='add_note'),

    path('view/<int:id>/', views.view_note, name='view_note'),

    path('edit/<int:id>/', views.edit_note, name='edit_note'),

    path('delete/<int:id>/', views.delete_note, name='delete_note'),

    path(
        'category/<str:category>/',
        views.category_notes,
        name='category_notes'
    ),

    path(
        'add-category/',
        views.add_category,
        name='add_category'
    ),
]