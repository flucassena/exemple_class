from django_filters import rest_framework as filters

from api import models

# Filtros de pesquisa
LIKE = 'unaccent__icontains'
ICONTAINS = 'icontains'
UNACCENT_IEXACT = 'unaccent__iexact'
EQUALS = 'exact'
STARTS_WITH = 'startswith'
GT = 'gt'
LT = 'lt'
GTE = 'gte'
LTE = 'lte'
IN = 'in'


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Author
        fields = ['name']


class AlbumFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr=LIKE)
    date = filters.DateFilter(lookup_expr=GTE)
    author = filters.CharFilter(field_name='author__name', lookup_expr=LIKE)

    class Meta:
        model = models.Album
        fields = ['title', 'date', 'author']


class MusicFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr=LIKE)
    duration = filters.DurationFilter(lookup_expr=GT)
    date = filters.DateFilter(field_name='album__date', lookup_expr=GTE)
    album = filters.CharFilter(field_name='album__title', lookup_expr=LIKE)

    class Meta:
        model = models.Music
        fields = ['title', 'duration', 'album']
