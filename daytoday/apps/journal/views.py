# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.http import Http404

from entrycalendar import EntryCalendar

from apps.journal.models import Entry
from apps.journal.forms import EntryForm
import datetime


class MyStruct(object):
    """ Attributes are added at view """


@login_required
def show_day(request, year, month, day):
    # Get the date
    date = datetime.date(int(year), int(month), int(day))
    if date > datetime.date.today():
        return render(request, "journal/future_day.html", {'date': date})

    # Find todays entry
    try:
        entry = Entry.objects.filter(user=request.user).get(date=date)
    except Entry.DoesNotExist:
        return HttpResponseRedirect(reverse(edit_day, args=(month, day, year)))
        entry = Entry(user=request.user, date=date)

    # Return it
    return render(request, "journal/day.html",
        {'date': date, 'entry': entry})


@login_required
def edit_day(request, year, month, day):
    # Get the date
    date = datetime.date(int(year), int(month), int(day))
    if date > datetime.date.today():
        return render(request, "journal/future_day.html", {'date': date})

    # Find todays entry
    try:
        entry = Entry.objects.filter(user=request.user).get(date=date)
    except Entry.DoesNotExist:
        entry = Entry(user=request.user, date=date)

    # Handle the posting
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['date'] = date
        entry_form = EntryForm(form_data, instance=entry)
        if entry_form.is_valid():
            valid_entry = entry_form.save(commit=False)
            valid_entry.save()
            return HttpResponseRedirect(reverse(show_day, args=(month, day, year)))
    else:
        entry_form = EntryForm(instance=entry)

    # Return it
    return render(request, "journal/edit_day.html",
        {'date': date, 'form': entry_form})
