from django.shortcuts import render
from trackerapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.
@api_view(['GET'])
def get_category(request):
    if request.method=='GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_category(request):
    if request.method=='POST':
        serializer = CategorySerializer(data=request.data)
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def add_expense(request):
    if request.method=='POST':
        Expenses = Expenses.objects.all()
        serializer = ExpenseSerializer(Expenses,many=True)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def delete_expense(request,id):
        Expenses = Expenses.objects.all()
        serializer = ExpenseSerializer(Expenses,many=True)
        return Response(serializer.data)
#one comment for push check

