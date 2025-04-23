from django.db.models import Func


class ILike(Func):
    function = 'ILIKE'
