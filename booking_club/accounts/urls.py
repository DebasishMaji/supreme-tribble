from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import re_path
from django.conf.urls import include
from .views import FacebookLogin
from rest_auth.views import PasswordResetConfirmView
from .views import GenericRegisterView

urlpatterns = [
    re_path(r'', include('rest_auth.urls')),
    re_path(r'^registrations/', include('rest_auth.registration.urls'), name=''),
    re_path(r'^registration/', GenericRegisterView.as_view()),
    re_path(r'^api-token-refresh/', refresh_jwt_token),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    # re_path(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    # re_path(r'^password/reset/', include('rest_auth.registration.urls'), name=''),
    # re_path(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm')
    re_path(r'^', include('django.contrib.auth.urls'))
]

