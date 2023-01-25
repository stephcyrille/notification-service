from rest_framework import serializers
from .models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"

    def validate(self, data):
        """
        Check if the email sender is the same as global config sender before finish.
        """
        if data['sender'] == '':  # TODO Set the global sender value as value check
            raise serializers.ValidationError("Please fill the good system sender")
        return data


class SignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    receiver = serializers.EmailField(required=True)
    confirmation_url = serializers.CharField(required=True)

    def create(self, validated_data):
        return ""  # Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.confirmation_url = validated_data.get('confirmation_url', instance.confirmation_url)
        instance.save()
        return instance
