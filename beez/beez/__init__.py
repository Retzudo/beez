__version__ = '0.7.3-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
