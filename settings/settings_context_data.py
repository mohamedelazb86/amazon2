from .models import Home

def get_context_data(request):
    data=Home.objects.last()
    return {'settings_data': data}