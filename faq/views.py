from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer


@api_view(['GET'])
def get_faqs(request):
    """Return FAQs in the requested language (fallback to English if missing)."""
    lang = request.query_params.get('lang', 'en')
    cache_key = f'faqs_{lang}'
    cached_faqs = cache.get(cache_key)

    if cached_faqs:
        return JsonResponse(cached_faqs, safe=False)

    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True, context={'request': request})
    cache.set(cache_key, serializer.data, timeout=3600)  # Cache for 1 hour
    return JsonResponse(serializer.data, safe=False)
