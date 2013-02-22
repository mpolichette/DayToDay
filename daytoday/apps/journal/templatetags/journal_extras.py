from django import template
import datetime
from apps.journal.entrycalendar import EntryCalendar
import calendar
#from apps.journal.models import Entry

register = template.Library()


@register.filter(name='rating_display')
def rating_display(entry, punct):
    if punct in ['auto']:
        if entry.rating in ['terrible', 'awesome']:
            return '{}!'.format(entry.get_rating_display())
        if entry.rating in ['bad', 'good']:
            return '{}.'.format(entry.get_rating_display())
        else:
            return entry.get_rating_display()
    else:
        return '{}{}'.format(entry.get_rating_display(), punct)

@register.assignment_tag
def get_today():
    return datetime.date.today()


@register.simple_tag
def calendar(date, entries=None):
    calendar = EntryCalendar(date)
    return calendar.formatmonth(int(date.year), int(date.month))
