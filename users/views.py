from django.http import HttpResponseRedirect
from .models import User
from .forms import UserForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404


def index(request):
    user_list = User.objects.order_by("id")

    return render(request, 'users/list.html', {'user_list': user_list})


def add(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.first_name = request.POST.get('first_name', '')
        instance.last_name = request.POST.get('last_name', '')
        instance.email = request.POST.get('email', '')
        new_user = User(first_name=instance.first_name, last_name=instance.last_name, email=instance.email)
        new_user.save()
        return HttpResponseRedirect('')

    return render(request, 'users/index.html', {'form': form})


def detail(request, user_id=None):
    context = {'user': get_object_or_404(User, pk=user_id),
               'sub_template': 'users/list.html'}

    return render(request, 'users/index.html', context)


def edit(request, user_id):
    # form = UserForm(request.POST or None)
    # if form.is_valid():
    #     # instance = form.save(commit=False)
    #     user = get_object_or_404(User, pk=user_id)
    #     user.first_name = request.POST.get('first_name', '')
    #     user.last_name = request.POST.get('last_name', '')
    #     user.email = request.POST.get('email', '')
    #     new_user = User(first_name=user.first_name, last_name=user.last_name, email=user.email)
    #     new_user.save()
    #     return HttpResponseRedirect('')
    # return render(request, 'users/index.html', {'form': form})
    # if user_id != 0:
    user = get_object_or_404(User, pk=user_id)

    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.email = request.POST["email"]
    user.save()

    return HttpResponseRedirect(reverse('index'))


def delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('index'))
