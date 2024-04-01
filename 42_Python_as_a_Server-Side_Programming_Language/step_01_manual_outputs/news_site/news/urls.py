from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>/', views.articles_detail, name='articles_detail'),
]