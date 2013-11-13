"""
reinitialize the test user account (and clean up)
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = 'reinitialize the test user'

    def handle_noargs(self, **options):
        try:
            u = User.objects.get(username='test')
            # delete test user and (via CASCADE behaviour) everything that
            # points to it (has user as ForeignKey), e.g. via created_by.
            u.delete()
        except User.DoesNotExist:
            pass
        # create a fresh test user
        u = User.objects.create_user('test', settings.DEFAULT_FROM_EMAIL, 'test')
        u.save()
        self.stdout.write('Successfully reinitialized the test user')
