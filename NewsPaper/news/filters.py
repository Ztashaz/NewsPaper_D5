import django
import django_filters
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, \
    DateFromToRangeFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Author, Category


# создаём фильтр
class PostFilter(FilterSet):
    date = django_filters.DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label="Дата от",
        widget=django.forms.DateInput(attrs={'type': 'date'})
    )
    author = ModelChoiceFilter(queryset=Author.objects.all(), label="Автор")
    category = ModelChoiceFilter(field_name='postCategory', queryset=Category.objects.all(), label="Категория")
    title = CharFilter(lookup_expr='icontains', label="Заголовок содержит")


    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = ['date', 'author', 'category', 'title']  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)