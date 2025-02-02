from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn')
    search_fields = ('question', 'question_hi', 'question_bn')


admin.site.register(FAQ, FAQAdmin)
