from .models import Category
from django.db.models import Count


# src = https://able.bio/rhett/how-to-order-by-count-of-a-foreignkey-field-in-django--26y1ug1


def menucategory(request):
    # categories = Category.objects.all()\
    #     .annotate(num_post=Count('post'))\
    #     .order_by('-num_post')

    category_3 = Category.objects.all()\
        .annotate(num_post=Count('post'))\
        .order_by('-num_post')[:3]
        
    rest_category = Category.objects.all()\
        .annotate(num_post=Count('post'))\
        .order_by('-num_post')[3:]
    context = {
        'category_3' : category_3,
        'rest_category': rest_category,
        # 'categories':categories
    }
    return context


