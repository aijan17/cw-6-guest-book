from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import GuestForm
from webapp.models import Guest


def guest_list(reguest):
    guests = Guest.objects.all().filter(status='active').order_by('-cread_date')
    return render(reguest, 'guest_list.html', {'guests': guests})


def get_search(request):
    query = request.GET['query']
    guests = Guest.objects.all().filter(status='active').order_by('-cread_date')
    if query:
        guests = Guest.objects.filter(name__icontains=query)

    return render(request, 'guest_list.html', {"guests": guests})


def create_guest(request):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'create_view.html', context={'form': form})

    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest = Guest.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                text=form.cleaned_data.get('text'),
            )
            return redirect('guest-list')
        return render(request, 'create_view.html', context={'form': form})


def update_view(request, id):
    guest_update = get_object_or_404(Guest, id=id)

    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guest_update.name,
            'email': guest_update.email,
            'text': guest_update.text,
        })
        return render(request, 'update_view.html', context={'form': form, 'guest_update': guest_update})

    elif request.method == 'POST':
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest_update.name = form.cleaned_data.get("name")
            guest_update.email = form.cleaned_data.get("email")
            guest_update.text = form.cleaned_data.get("text")
            guest_update.save()
            return redirect('guest-list')

        return render(request, 'create_view.html', context={'form': form})


def remove_view(request, id):
    guest = get_object_or_404(Guest, id=id)

    if request.method == 'GET':
        guest.delete()
    return redirect('guest-list')
