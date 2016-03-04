from __future__ import unicode_literals, absolute_import

from django.apps import AppConfig


class ExampleConfig(AppConfig):
    name = 'example'

    def ready(self):
        from . import handlers  # noqa
