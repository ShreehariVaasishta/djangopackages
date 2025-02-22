# Make our own testrunner that by default only tests our own apps

from django.conf import settings
from django.test.runner import DiscoverRunner


class OurTestRunner(DiscoverRunner):
    def build_suite(self, test_labels, *args, **kwargs):
        return super().build_suite(
            test_labels or settings.PROJECT_APPS, *args, **kwargs
        )
