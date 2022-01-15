from rest_framework import serializers
from .models import MyUser


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'password']
        # for hiding password to be serialize in postman
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # for saving password in hash form

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
