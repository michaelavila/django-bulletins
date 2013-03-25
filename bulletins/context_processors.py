import models

def bulletins(request):
    try:
        direct = models.DirectBulletin.objects.filter(
            recipient=request.user
        )
    except AttributeError:
        direct = []

    return {
        'bulletins': {
            'global': models.GlobalBulletin.objects.all(),
            'direct': direct
        }
    }
