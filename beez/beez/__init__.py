__version__ = '0.3.1-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
