import calendar

import requests
from celery.task import task

from allauth.socialaccount.models import SocialToken

from .models import User, UserJob, UserSocialLink


@task()
def populate_user(pk):
    user = User.objects.get(pk=pk)
    token = SocialToken.objects.get(account__user__pk=pk)
    headers = {'Authorization': f'Bearer {token.token}'}
    url = 'https://api.linkedin.com/v1/people/~:(headline,summary,location,positions)?format=json'
    req = requests.get(url, headers=headers)
    if req.status_code == requests.codes.ok:
        extra_data = token.account.extra_data
        data = req.json()
        extra_data.update(**data)
        positions = extra_data.get('positions', [])
        user.extra_data = extra_data
        user.headline = extra_data.get('headline', '')
        user.location = extra_data.get('location', {}).get('name', '')
        user.summary = extra_data.get('summary', '')
        
        if positions:
            for position in positions.get('values'):
                start_date = position.get('startDate')
                is_current = position.get('isCurrent')
                defaults = {
                    'role': position.get('title'),
                    'company_name': position.get('company', {}).get('name', ''),
                    'is_current': is_current,
                    'from_month': calendar.month_name[start_date.get('month')],
                    'from_year': start_date.get('year'),
                    'user': user
                }
                if not is_current:
                    end_date = positions.get('endDate')
                    defaults.update(
                        from_month=calendar.month_name[end_date.get('month')],
                        from_year=end_date.get('year')
                    )
                UserJob.objects.update_or_create(**defaults)

        UserSocialLink.objects.update_or_create(
            name='linkedin',
            url=extra_data.get('publicProfileUrl', ''),
            user=user
        )
        user.save()
