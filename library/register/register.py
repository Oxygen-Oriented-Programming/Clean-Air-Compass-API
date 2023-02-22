from rest_framework.authtoken.models import Token
from default_locations.models import DefaultLocation
from accounts.models import User
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ObjectDoesNotExist


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)
    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            new_user = User.objects.get(email=email)

            registered_user = User.objects.get(email=email)
            registered_user.check_password(settings.SOCIAL_SECRET)
            default_location = "seattle"
            try:
                print(DefaultLocation.objects.get(user=registered_user))
            except ObjectDoesNotExist:
                pass
            # print(DefaultLocation.objects.get(user=registered_user).first())
            Token.objects.filter(user=registered_user).delete()
            Token.objects.create(user=registered_user)
            new_token = list(Token.objects.filter(
                user_id=registered_user).values("key"))
            print(registered_user.id)
            if default_location:
                return {
                    'user_id': registered_user.id,
                    'username': registered_user.username,
                    'default_location': default_location,
                    'email': registered_user.email,
                    'tokens': str(new_token[0]['key'])}
            else:
                return {
                    'user_id': registered_user.id,
                    'username': registered_user.username,
                    'email': registered_user.email,
                    'tokens': str(new_token[0]['key'])}

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': email, 'email': email,
            'password': settings.SOCIAL_SECRET
        }
        user = User.objects.create_user(**user)
        user.is_active = True
        user.auth_provider = provider
        user.save()
        new_user = User.objects.get(email=email)
        new_user.check_password(settings.SOCIAL_SECRET)
        Token.objects.create(user=new_user)
        new_token = list(Token.objects.filter(user_id=new_user).values("key"))
        return {
            'user_id': new_user.id,
            'email': new_user.email,
            'username': new_user.username,
            'tokens': str(new_token[0]['key']),
        }