from django.conf import settings


class NULL:
    pass


class SettingsOverride:
    """
    Overrides Django settings within a context and resets them to their initial
    values on exit.

    Example::

        with SettingsOverride(DEBUG=True):
            # do something
    """

    def __init__(self, **overrides):
        self.overrides = overrides

    def __enter__(self):
        self.old = {}
        for key, value in list(self.overrides.items()):
            self.old[key] = getattr(settings, key, NULL)
            setattr(settings, key, value)

    def __exit__(self, type, value, traceback):
        for key, value in list(self.old.items()):
            if value is not NULL:
                setattr(settings, key, value)
            else:
                delattr(settings, key)  # do not pollute the context!
