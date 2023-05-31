from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('calc/', calc, name='calc'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/<int:id>', blog_detail, name='blog-detail'),
]
