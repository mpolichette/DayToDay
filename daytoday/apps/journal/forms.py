from django import forms
from django.forms.widgets import HiddenInput, RadioSelect
from django.forms import ModelForm
from apps.journal.models import Entry
from django.utils.safestring import mark_safe


# class DayRatingForm(forms.Form):
#     rating = forms.IntegerField(min_value=1, max_value=5)
#     summary = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':'', 'class':'span8'}), required=False)


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('date', 'rating', 'summary')
        widgets = {
            'date': HiddenInput,
            'rating': HiddenInput,
            'summary': forms.Textarea(attrs={'rows': 4, 'cols': '', 'class': 'span8'}),

        }

    edit_mode = False
    
    def needs_rating(self):
        return self.instance.rating == None

    def in_edit_mode(self):
        return self.edit_mode

    # def rating_buttons(self):
    #     classes = ["row"]
    #     if self.instance and self.instance.rating:
    #         classes += ["hidden"]
    #     html = ["<div class={}>".format(' '.join(classes))]
    #     html += ['<div class="btn-toolbar span7">']
    #     html += ['<button class="btn btn-large btn-darkred" type="submit" name="rating" value="1">Terrible</button>']
    #     html += ['<button class="btn btn-large btn-lightred" type="submit" name="rating" value="2">Bad</button>']
    #     html += ['<button class="btn btn-large btn-yellow" type="submit" name="rating" value="3">Meh...</button>']
    #     html += ['<button class="btn btn-large btn-lightgreen" type="submit" name="rating" value="4">Good</button>']
    #     html += ['<button class="btn btn-large btn-darkgreen" type="submit" name="rating" value="5">Awesome</button>']
    #     html += ['</div></div>']
    #     return mark_safe(''.join(html))