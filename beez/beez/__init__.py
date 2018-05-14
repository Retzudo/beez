__version__ = '0.6.0-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
