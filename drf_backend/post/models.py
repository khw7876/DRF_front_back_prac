# get으로 posting 가져오기, post로 posting 구현하기
from django.db import models

class Post(models.Model):

    class Meta:
        db_table = "post"
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField('제목',max_length=20)
    content = models.TextField('설명', max_length=128)
    create_date = models.DateField('생성 날짜',auto_now_add=True)
    edit_date = models.DateField("수정 날짜", auto_now=True)
