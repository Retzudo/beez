__version__ = '0.8.1-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
