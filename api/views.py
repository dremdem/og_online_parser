from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.parsers.utils import parse_url


@api_view(['POST'])
def parse(request):

    return Response(parse_url(request.data))

# Create your views here.
