from . common import *

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='%&n+ix#n^7i(-1(#+nhok^2v@gy#42yyta^bzz*fwrd7&^&s%1')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

DEBUG_TOOLBAR_PATCH_SETTINGS = False
MIDDLEWARE += ['config.middleware.AdaptedTo110DebugMiddleware',]
INSTALLED_APPS += ['django_extensions','debug_toolbar',]
INTERNAL_IPS = ['127.0.0.1', '107.170.83.208',]
