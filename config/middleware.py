from django.utils.deprecation import MiddlewareMixin
from debug_toolbar.middleware import DebugToolbarMiddleware


class AdaptedTo110DebugMiddleware(MiddlewareMixin, DebugToolbarMiddleware):
    pass
