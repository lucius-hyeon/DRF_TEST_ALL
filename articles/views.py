from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

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