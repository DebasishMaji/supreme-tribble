"""stalwart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


versioned_url_patterns = [
    # re_path(r'^(?P<version>v?[.0-9]+)/accounts/', include('accounts.urls'))
]

non_versioned_url_patterns = [
    re_path(r'^accounts/', include('accounts.urls')),
    re_path(r'^$', schema_view)
]

urlpatterns += versioned_url_patterns
urlpatterns += non_versioned_url_patterns
