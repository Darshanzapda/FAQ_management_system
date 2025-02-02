from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        request = self.context.get('request', None)
        lang = request.query_params.get('lang', 'en') if request else 'en'

        translated_data = instance.get_translated_text(lang)

        return {
            'id': instance.id,
            'question': translated_data['question'],
            'answer': translated_data['answer']
        }
