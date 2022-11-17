from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Article, Comment
from .serializers import ArticleSerializer,ArticleCommentSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        print("로그인 유저: ",request.user)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({"message": "게시글 등록 완료.", "result":serializer.data})
        else:
            return Response({"message":"실패", "result":serializer.errors})
        

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, article_id):
        print("article put")
        article = get_object_or_404(Article, author=request.user, pk=article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({"message":"수정 완료","result":serializer.data})
        else:
            return Response({"message":serializer.errors})
        
    def delete(self, request, article_id):
        print("article delete")
        article = get_object_or_404(Article, author=request.user, pk=article_id)
        print(article)
        article.delete()
        return Response({"message":"삭제 완료"})

class ArticleLike(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)

        if article.likes.filter(id=request.user.id).exists() == False:
            article.likes.add(request.user)
            result ='like'

        else:
            article.likes.remove(request.user)
            result ='unlike'
            
        return Response(result)
        
        
class ArticleComment(APIView):
    def get(self, request, article_id):
        print("comment get")
        comment = Comment.objects.filter(article_id=article_id)
        serializer = ArticleCommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def post(self, request, article_id):
        print("comment post")
        serializer = ArticleCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article_id=article_id)
            return Response(serializer.data)
        else:
            return Response({"message":serializer.errors})
    
    # 댓글 수정 기능
    def put(self, request, article_id, comment_id):
        print("comment put")
        comment = get_object_or_404(Comment, pk=comment_id, article_id=article_id, author=request.user)
        serializer = ArticleCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article_id=article_id)
            return Response({"message":"수정 완료"})
    
    def delete(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id, article_id=article_id, author = request.user)
        comment.delete()
        return Response({"message":'삭제 완료'})
        
