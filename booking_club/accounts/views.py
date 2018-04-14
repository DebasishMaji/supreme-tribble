# from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from django.shortcuts import render
from rest_auth.app_settings import create_token
from rest_auth.utils import jwt_encode
from rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from rest_auth.registration.views import RegisterView

# Create your views here.
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from .serializers import GenericRegisterSerializer
from django.conf import settings

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GenericRegisterView(RegisterView):
    serializer_class = GenericRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        # complete_signup(self.request._request, user,
        #                 allauth_settings.EMAIL_VERIFICATION,
        #                 None)
        return user
