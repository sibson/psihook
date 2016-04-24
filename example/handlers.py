from django.dispatch import receiver

import structlog

from psihook_debug.signals import psihook_debug

log = structlog.get_logger()


@receiver(psihook_debug)
def handle_debug(sender, **kwargs):
    log.debug('debug hook called', **kwargs)
