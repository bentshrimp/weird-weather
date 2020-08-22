from django.contrib import admin

# 모델을 admin 사이트에 등록
from django.contrib import admin
from polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)