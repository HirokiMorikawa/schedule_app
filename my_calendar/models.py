from django.db import models

# Create your models here.


class Schedule(models.Model):
    # date = models.DateField()  # 日付
    start_time = models.DateTimeField()  # 開始時間
    end_time = models.DateTimeField()  # 終了時間
    company = models.CharField(max_length=128)  # 会社名n
    place = models.TextField()  # 場所


