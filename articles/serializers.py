from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('author',)

    author = serializers.SerializerMethodField()
    
    def get_author(self, obj):
        return obj.author.email