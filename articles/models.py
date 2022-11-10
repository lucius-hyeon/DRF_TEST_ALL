from django.db import models
from users.models import User

class Article(models.Model):
    class Meta:
        db_table = 'article'
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 테그, 좋아요 추가할 예정
    
    def __str__(self):
        return str(f'{self.title}')
    
