from django.db import models

# 데이터 베이스 정의
class Question(models.Model):
    question_text = models.CharField(max_length=200)        # 질문 텍스트(최대 길이 200자)
    pub_date = models.DateTimeField('data published')       # 질문한 날짜

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text