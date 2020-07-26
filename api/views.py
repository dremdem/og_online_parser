from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.parsers.utils import parse_url, get_parsers, get_last_n_urls


@api_view(['POST'])
def parse(request):
    """
    Base route for parsing url
    """
    try:
        data = parse_url(request.data)
        return Response(data, content_type='text/html; charset=utf-8')
    except Exception as e:
        return Response(data=str(e), exception=str(e), status=500)


@api_view(['GET'])
def parsers(request):
    """
    Get all parsers
    """
    return Response(get_parsers())


@api_view(['GET'])
def last_urls(request):
    """
    Get last urls
    """
    return Response(get_last_n_urls())


def index(request):
    """
    The only index page
    """
    return render(request, 'index.html')
