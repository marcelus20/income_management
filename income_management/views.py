from django.shortcuts import render
from rest_framework import viewsets
from .models import Users, Transactions, Description
from .serializers import UsersSerializers as u, TransactionsSerializer as t, DescriptionSerializer as d

# Create your views here.
class DescriptionView (viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = d

class TransactionView (viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = t

class UsersView (viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = u
