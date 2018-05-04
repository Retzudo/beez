__version__ = '0.5.3-alpha'


def version(request):
    return {
        'beez_version': __version__
    }
