from django import forms
from django.utils.translation import gettext as _
from django_filters import FilterSet
from django_filters.filters import BooleanFilter, ModelChoiceFilter
from task_manager.labels.models import Label
from task_manager.tasks.models import Task


class TaskFilter(FilterSet):
    personal_tasks = BooleanFilter(
        widget=forms.CheckboxInput,
        field_name='created_by',
        method='filter_personal_tasks',
        label=_('Only my tasks'),
    )

    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Label'),
    )

    def filter_personal_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(created_by=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'responsible', 'label', 'personal_tasks']
