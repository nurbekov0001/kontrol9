from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from webapp.forms import SearchForm, PhotoDeleteForm, PhotoForm

from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from webapp.models import Photo, Album


class PhotoIndexView(ListView):

    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at',)
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(PhotoIndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(signature__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):

        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['search_form'] = self.form
        # print(context)
        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        photo = Photo.objects.all()
        if self.request.user.groups.filter(name='Moderator').exists():
            context['reviews'] = photo
            return context
        else:
            context['reviews'] = photo.filter(choice='public')
        return context



class PhotoView(DetailView):
    model = Photo
    template_name = 'photo/view.html'
    context_object_name = 'photo'


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse('photo:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):

    template_name = 'photo/delete.html'
    model = Photo
    context_object_name = 'photo'
    permission_required = 'webapp.delete_photo'
    success_url = reverse_lazy('photo:photo_list')


class PhotoCreateView(PermissionRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/create.html'
    form_class = PhotoForm
    permission_required = 'webapp.change_photo'

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author_album = self.request.user
        album.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('photo:photo_view', kwargs={'pk': self.object.pk})


