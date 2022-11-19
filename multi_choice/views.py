from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import multi_choice
from .serializers import mcSerializer
import random

# Create your views here.

@api_view(['GET'])
def showQuiz(request):
    totalQuizs = multi_choice.objects.all()
    serializer = mcSerializer(totalQuizs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomQuiz(requser):
    totalQuizs = multi_choice.objects.all()
    count = totalQuizs.count()
    randomQuiz = random.sample(list(totalQuizs),count)
    serializer = mcSerializer(randomQuiz, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")
