from django.conf import settings
from rest_framework import serializers
from library.socaillib import github
from library.socaillib import google
from library.register.register import register_social_user
from rest_framework.exceptions import *


class GithubSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""

    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = github.Github.validate(auth_token)

        try:
            email = user_data["email"]
            provider = "github"
        except:
            raise serializers.ValidationError(
                "The token  is invalid or expired. Please login again."
            )
        return register_social_user(
            provider=provider, user_id=None, email=email, name=None
        )

class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )
        print(user_data['aud'])
        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:

            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)