from django.contrib.auth.models import User
from rest_framework import serializers



class Registration(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwrgs ={
            'password':{'write_only':True}
        }
    
    def save(self):
        password=self.validated_data['password']
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
        