'''
django admin site에 등록하기 위한 문서
'''
from django.contrib import admin
from .models import Question

# Register your models here.

admin.site.register(Question)