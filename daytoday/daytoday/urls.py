from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from datetime import date;
admin.autodiscover()

from django.contrib.auth.views import login, logout_then_login

# Admin URLs
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    )

# Login/Logout
urlpatterns += patterns('',
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    )

# Main and account
urlpatterns += patterns('apps.account.views',
    url(r'^$', lambda x: HttpResponseRedirect('/today/'))
    )

# Journal

#/day/edit/11-25-2012
#/day/11-25-2012/edit
#/editday/11-25-2012

today = date.today()
urlpatterns += patterns('apps.journal.views',
    url(r'^today/$', 'show_day', {'year':today.year, 'month':today.month, 'day':today.day}, name='today'),
    url(r'^day/(?P<month>\d{1,2})-(?P<day>\d+)-(?P<year>\d{4})/$', 'show_day', name='day'),
    url(r'^day/(?P<month>\d{1,2})-(?P<day>\d+)-(?P<year>\d{4})/edit/$', 'edit_day', name='edit_day')
    )
