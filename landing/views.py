from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import SubscriberForm
from .models import Subscriber  

def landing(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            
            send_mail(
                subject="Welcome to TrackrHub! 🎉",
                message="Thank you for joining our waitlist! We'll notify you as soon as we launch.",
                from_email=None,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )

            messages.success(request, "You’ve been added to the waitlist! Check your e-mail.")
            return redirect("landing")
    else:
        form = SubscriberForm()

    subscriber_count = 17 + Subscriber.objects.count()

    return render(request, "landing/index.html", {
        "form": form,
        "subscriber_count": subscriber_count,
    })
