from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.parsers.utils import parse_url


@api_view(['POST'])
def parse(request):
    """
    Base route for parsing url
    """
    return Response(parse_url(request.data))


def index(request):
    """
    The only index page
    """
    return render(request, 'index.html')

