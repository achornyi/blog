from django.urls import path, include
from .views import ArticleListView, ArticleDetailsView


urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>/', ArticleDetailsView.as_view()),
]
