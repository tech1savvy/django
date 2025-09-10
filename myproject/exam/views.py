from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback

@login_required
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                rating=form.cleaned_data['rating'],
                comments=form.cleaned_data['comments']
            )
            return redirect('thanks')  # or wherever you want after submission
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def thanks_view(request):
    return render(request, 'thanks.html')
