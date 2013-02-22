import calendar
from datetime import date
from itertools import groupby
from django.core.urlresolvers import reverse

from django.utils.html import conditional_escape as esc

class EntryCalendar(calendar.HTMLCalendar):

    def __init__(self, selected_day=None):
        super(EntryCalendar, self).__init__(calendar.SUNDAY)
        self.selected_day = selected_day

    def formatday(self, day, weekday):
        if day != 0:
            # Generate a link to that day
            cur_date = date(self.year, self.month, day)
            link = reverse('day', args=(self.month, day, self.year))
            # Add the day of week class
            cssclass = [self.cssclasses[weekday]]
            # If it is today, apply today class
            if date.today() == cur_date:
                cssclass += ['today']
                link = "/today"
            if cur_date == self.selected_day:
                cssclass += ["selected"]
            # Build the html
            return self.day_cell(' '.join(cssclass), day, link)
        # Return a no-day item
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EntryCalendar, self).formatmonth(year, month)

    # def group_by_day(self, entries):
    #     field = lambda workout: workout.performed_at.day
    #     return dict(
    #         [(day, list(items)) for day, items in groupby(entries, field)]
    #     )

    def day_cell(self, cssclass, body, link=None):
        if link:
            body = '<a href="{}">{}</a>'.format(link, body)
        return '<td class="{}">{}</td>'.format(cssclass, body)
