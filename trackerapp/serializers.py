from rest_framework import serializers
from trackerapp.models import Category , Expenses

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields='__all__'