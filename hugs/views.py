from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hug
from django.contrib.auth.models import User

from django.contrib import messages

@login_required
def send_hug(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    Hug.objects.create(sender=request.user, receiver=receiver)
    messages.success(request, f'Hug sent to {receiver.username} successfully!')  # Success message
    return redirect('hug_page')  # Redirect back to the main hug page


@login_required
def hug_page(request):
    users = User.objects.exclude(id=request.user.id)  # List of users excluding the logged-in user
    last_received_hug = Hug.objects.filter(receiver=request.user).order_by('-id').first()  # Hugs received by the current user
    return render(request, 'hugs/hug_page.html', {
        'users': users,
        'last_received_hug': last_received_hug,
    })

