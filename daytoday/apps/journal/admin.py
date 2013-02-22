from django.contrib import admin
from apps.journal.models import Entry,Activity,ActivityRecord
admin.site.register(Activity)
admin.site.register(ActivityRecord)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'user', 'date', 'id')
    list_filter = ('user',)

    def identifier(self, entry):
        return "{date} by {user}".format(user=entry.user, date=entry.date.strftime('%b %d'))
    identifier.short_description = "Entry"
admin.site.register(Entry, EntryAdmin)