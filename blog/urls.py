from django.urls import path
from .views import allblogs, detailed_blog

urlpatterns = [
    path('', allblogs, name='allblogs'),
    path('<int:blog_id>/', detailed_blog, name='detailed_blog'),
]
