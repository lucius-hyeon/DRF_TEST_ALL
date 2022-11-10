from django.urls import path
from .views import ArticleView

urlpatterns = [
    path('list/',ArticleView.as_view(), name='article_list'),
]
