from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.models import Profile
from .forms import MyUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator


from accounts.models import Profile


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('photo:photo_list')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('photo:photo_list')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('photo:photo_list')
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 1

    def get_context_data(self, **kwargs):
        projects = self.object.projects.all()
        paginator = Paginator(projects, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['photo'] = page.object_list

        kwargs['is_paginate'] = page.has_other_pages()
        return super().get_context_data(**kwargs)

