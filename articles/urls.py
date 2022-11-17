from django.urls import path
from .views import ArticleView, ArticleLike, ArticleDetailView,ArticleComment

urlpatterns = [
    path('list/',ArticleView.as_view(), name='article_list'),
    path('<int:article_id>/',ArticleDetailView.as_view(), name='article_detail_view'),
    path('<int:article_id>/liker/', ArticleLike.as_view(), name='article_like'),
    path('<int:article_id>/comment/', ArticleComment.as_view(), name="article_comment"),
    path('<int:article_id>/comment/<int:comment_id>/', ArticleComment.as_view(), name="article_comment_update"),
]
