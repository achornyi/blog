from django_filters import rest_framework as filters
from articles.models import Article


class TagsFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name='tags', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['tags']
