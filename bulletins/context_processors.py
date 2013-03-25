import models

def bulletins(request):
    return {
        'bulletins': {
            'global': models.GlobalBulletin.objects.all()
        }
    }
