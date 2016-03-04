from django.dispatch import receiver

from psihook_debug.signals import psihook_debug
from psihook_debug.tasks import log_signal


@receiver(psihook_debug)
def handle_debug(sender, **kwargs):
    log_signal.delay(kwargs['method'], kwargs['path'], kwargs['headers'], kwargs['payload'])
