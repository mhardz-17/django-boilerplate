# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskbuster_db',
        'USER': 'taskbuster',
        'PASSWORD': 'taskbuster',
    }
}

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    # DEBUG_TOOLBAR_PANELS = (
    #     'debug_toolbar.panels.version.VersionDebugPanel',
    #     'debug_toolbar.panels.timer.TimerDebugPanel',
    #     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    #     'debug_toolbar.panels.headers.HeaderDebugPanel',
    #     #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
    #     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    #     'debug_toolbar.panels.sql.SQLDebugPanel',
    #     'debug_toolbar.panels.template.TemplateDebugPanel',
    #     'debug_toolbar.panels.cache.CacheDebugPanel',
    #     'debug_toolbar.panels.signals.SignalDebugPanel',
    #     'debug_toolbar.panels.logger.LoggingPanel',
    # )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }