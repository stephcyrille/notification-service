from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    receiver = serializers.EmailField(required=True)
    confirmation_url = serializers.CharField(required=True)

    def create(self, validated_data):
        return ""  # Comment(**validated_data)

    def update(self, instance, validated_data):
        return ""


class SigninSerializer(serializers.Serializer):
    receiver = serializers.EmailField(required=True)

    def create(self, validated_data):
        return ""  # Comment(**validated_data)

    def update(self, instance, validated_data):
        return ""


class PasswordResetRequestSerializer(serializers.Serializer):
    receiver = serializers.EmailField(required=True)
    reset_url = serializers.URLField(required=True)

    def create(self, validated_data):
        return ""  # Comment(**validated_data)

    def update(self, instance, validated_data):
        return ""
