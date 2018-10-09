from rest_framework import serializers

from .models import Description, Users, Transactions

class DescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Description
        fields = ('id', 'name', 'brief_description')

class UsersSerializers(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email', 'user_permissions')

class TransactionsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transactions
        fields = ('id', 'date', 'income', 'expense', 'diary_balance', 'total_balance', 'description', 'user')