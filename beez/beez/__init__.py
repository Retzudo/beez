__version__ = '0.3.0-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
