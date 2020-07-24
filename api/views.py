from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.parsers.utils import parse_url, get_parsers


@api_view(['POST'])
def parse(request):
    """
    Base route for parsing url
    """
    return Response(parse_url(request.data))


@api_view(['GET'])
def parsers(request):
    """
    Get all parser
    """
    return Response(get_parser())


def index(request):
    """
    The only index page
    """
    return render(request, 'index.html')

