from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets,permissions,generics
from rest_framework.viewsets import ModelViewSet
from django.views.generic import CreateView
from django.core.mail import send_mail



class HeadView(APIView):
    def get(self,*args,**kwargs):
        name = Header.objects.all()
        serializer = HeaderSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class HeadisView(viewsets.ModelViewSet):
    queryset = Headerdis.objects.all()
    serializer_class = HeaderdisSerialzers


class FeedBackView(APIView):
    serializer_class = ContactSerailizer

    def post(self, request, *args, **kwargs):
        serializer_class = ContactSerailizer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get('name')
            from_email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            try:
                send_mail(f'От {name} | {subject}',message, from_email, ['zumc4847@gmail.com'])
            except AssertionError:
                return Response({'Failed to send'})
        return Response({"success": "Sent"})

class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)

class CareerView(APIView):
    def get(self,*args,**kwargs):
        name = Career.objects.all()
        serializer = CareerSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Job_fairView(APIView):
    def get(self,*args,**kwargs):
        name = Job_fair.objects.all()
        serializer = JobfairSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Reception_campaignView(APIView):
    def get(self,*args,**kwargs):
        name = Reception_campaign.objects.all()
        serializer = Reception_campaignSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Forms_of_trainingView(APIView):
    def get(self,*args,**kwargs):
        name = Forms_of_training.objects.all()
        serializer = Forms_of_trainingSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Description_formView(APIView):
    def get(self,*args,**kwargs):
        name = Description_form.objects.all()
        serializer = Description_formSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class Open_dayView(APIView):
    def get(self,*args,**kwargs):
        name = Open_day.objects.all()
        serializer = Open_daySerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class News_blogView(APIView):
    def get(self,*args,**kwargs):
        name = News_Blog.objects.all()
        serializer = News_blogSerializer(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
