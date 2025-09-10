from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    rating = forms.IntegerField(min_value=1, max_value=5, required=True)
    comments = forms.CharField(widget=forms.Textarea, required=False)