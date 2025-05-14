from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


@api_view(['GET'])
def healthcheck(request):
  return Response({"status": "ok"}, status=200)


def index(request):
  return HttpResponse("Hello, world. This is the index page.")
