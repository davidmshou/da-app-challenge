from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from .forms import UserForm
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, there. This is the index of all our users.")
    user_list = User.objects.order_by("first_name")
    # for user in users:
    #     user_list = users(list)
    # lines = []
    # for user in user_list:
    #     lines.append({
    #         "First": user.first_name,
    #         "Last": user.last_name,
    #         "Email": user.email,
    #     })
    #     return lines

    # return HttpResponse(user_list)
    return render(request, 'users/list.html', {'user_list': user_list})

    # user_list = User.objects.all()
    # template = loader.get_template("users/index.html")
    # context = RequestContext(request, {
    #     "user_list": user_list,
    # })
    # return HttpResponse(template.render(context))


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

    # newUser = User(first_name=request.POST["first_name"],
    #                last_name=request.POST["last_name"],
    #                email=request.POST["email"],)
    # newUser.save()
    # return HttpResponseRedirect(reverse("index"))


# def edit(request):
#     user = User.objects.get(email=request.POST["originalEmail"])
#     if request.POST["submitButton"] == "Update":
#         user.first_name = request.POST["first_name"]
#         user.last_name = request.POST["last_name"]
#         user.email = request.POST["email"]
#         user.save()
#     elif request.POST["submitButton"] == "Delete":
#         user.delete()

#     return HttpResponseRedirect(reverse("index"))


def delete(request):
    users = User.objects.get(first_name=User.first_name)
    for user in users:
        if request.POST("delete_button"):
            user.delete()
    # return HttpResponse("Delete")
    # user_list = User.objects.all()
    # for user in user_list:

    # return render(request, 'users/delete.html', {'user_list': user_list})
