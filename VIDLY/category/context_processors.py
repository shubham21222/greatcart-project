<<<<<<< HEAD
from .models import Category

def menu_links(request):
    links = Category.objects.all()
=======
from .models import Category

def menu_links(request):
    links = Category.objects.all()
>>>>>>> 1baa7bd3e80870e161f11c7e57ef726649ae0d87
    return dict(links=links)