from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('categories/<int:categories_id>/', views.categories, name='categories'),
    path('results/<int:results_id>/', views.results, name='results'),
    path('locations/', views.locations, name='locations')
]
