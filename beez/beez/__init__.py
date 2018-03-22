__version__ = '0.1.0-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
