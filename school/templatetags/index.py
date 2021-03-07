from django import template

from school.models import Result

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def getitem(indexable, i):
    return indexable[i]

@register.filter
def gave_exam(indexable):
    from school.models import Result
    result = Result.objects.filter(student__id=indexable.pk)
    if result:
        return True
    else:
        return False
    