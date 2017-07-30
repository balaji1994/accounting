from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import include, url
from django.conf import settings

from .views import userlogin

urlpatterns = [
    url(r'^validate/$', userlogin.validate),
    url(r'^checkuser/$', userlogin.check_user),
    url(r'^checkaccno/$', userlogin.check_accountno),
    url(r'^signup/$', userlogin.signup),
    url(r'^sendemail/$', userlogin.sendemail),
]
