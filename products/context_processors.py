from .models import Wishlist


def wishlist_count(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
        count = wishlist.products.count()
    else:
        count = 0
    return {'wishlist_count': count}
