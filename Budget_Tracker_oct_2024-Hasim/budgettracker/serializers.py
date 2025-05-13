from rest_framework import serializers
from .models import User, UserProfile, InputSave, Category, Income, Expense, Budget, EMI
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Set the password hash
        user.save()
        return user

# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number', 'address', 'date_of_birth']

# InputSave Serializer
class InputSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSave
        fields = ['id', 'name', 'number']

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'user']

# Income Serializer
class IncomeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer

    class Meta:
        model = Income
        fields = ['id', 'user', 'category', 'amount', 'date']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        income = Income.objects.create(category=category, **validated_data)
        return income

# Expense Serializer
class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer

    class Meta:
        model = Expense
        fields = ['id', 'user', 'category', 'amount', 'date', 'description']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        expense = Expense.objects.create(category=category, **validated_data)
        return expense

# Budget Serializer
class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer

    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'limit', 'period']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        budget = Budget.objects.create(category=category, **validated_data)
        return budget

# EMI Serializer
class EMISerializer(serializers.ModelSerializer):
    class Meta:
        model = EMI
        fields = ['id', 'user', 'amount', 'due_date', 'description']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password")

        attrs['user'] = user  # Store the authenticated user
        return attrs