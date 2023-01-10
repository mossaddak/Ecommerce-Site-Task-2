from .models import ProductCategory
def categories(request):
    return {"ProductCategory":ProductCategory.objects.all()}
