import logging

from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from torre_test.users import tasks


logger = logging.getLogger(__name__)


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
    
    def get_login_redirect_url(self, request):
        path = "/{username}/"
        tasks.populate_user.apply_async(args=[request.user.pk])
        return path.format(username=request.user.username)


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request, sociallogin):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
