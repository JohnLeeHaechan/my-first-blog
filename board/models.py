from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # id            auto_increment                               자동 증가 컬럼
    title = models.CharField(max_length=200)                     # 게시판의 제목 컬럼
    sub_title = models.CharField(max_length=100)                 # 게시판의 종류 컬럼
    author = models.CharField(max_length=50)                     # 게시판의 작성자 컬럼
#    files = models.FileField(upload_to="photo/%Y/%m/%d", blank=True)
    files = models.ImageField(upload_to="photo/%Y%m%d", blank=True)
    content = models.TextField()                                 # 게시판의 게시글 컬럼
    created_date = models.DateTimeField(default=timezone.now)    # 게시판의 생성일 컬럼
    published_date = models.DateTimeField(blank=True, null=True) # 게시판의 수정일 컬럼
    view_count = models.IntegerField(default=0)                  # 게시판의 조회수 컬럼

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
