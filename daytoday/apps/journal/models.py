from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404
import datetime
# Create your models here.

DAY_RATING_CHOICES = (
    ('terrible', 'Terrible'),
    ('bad', 'Bad'),
    ('meh', 'Meh...'),
    ('good', 'Good'),
    ('awesome', 'Awesome'),
)

class Entry(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    entered_on = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=10, choices=DAY_RATING_CHOICES, default=None)
    summary = models.TextField(blank=True)

    unique_together = (("user", "date"),)

    def __unicode__(self):
        return "Entry[{id}] - {date} - {user}".format(id=self.id, user=self.user.username, date=self.date.strftime('%b %d, %Y'))

    def get_edit_url(self):
        return reverse('apps.journal.views.edit_day', args=(self.date.month, self.date.day, self.date.year))






class Activity(models.Model):
    name = models.CharField(max_length=50)


class ActivityRecord(models.Model):
    entry = models.ForeignKey(Entry)
    activity = models.ForeignKey(Activity)
    summary = models.TextField()
