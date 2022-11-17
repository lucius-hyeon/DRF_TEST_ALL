from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author',)

    author = serializers.SerializerMethodField()
    
    def get_author(self, obj):
        return obj.author.email
    

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'article', 'id')
        
        author = serializers.SerializerMethodField()
        
        def get_author(self, obj):
            return obj.user.email