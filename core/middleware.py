import structlog

LOGGER = structlog.get_logger()


class AddRequestIdMiddleware(object):

    def process_request(self, request):
        print { k: request.META[k] for k in request.META if k.startswith('HTTP')}
        request_id = request.META.get('HTTP_X_REQUEST_ID')
        if not request_id:
            return

        request.id = request_id

        global LOGGER
        LOGGER = LOGGER.new(request_id=request_id)
