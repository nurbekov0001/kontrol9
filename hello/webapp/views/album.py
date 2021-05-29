from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumView(DetailView):
    model = Album
    template_name = 'album/view.html'
    context_object_name = 'album'


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):

    template_name = 'album/delete.html'
    model = Album
    context_object_name = 'album'
    success_url = reverse_lazy('photo:photo_list')


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'album/update.html'
    form_class = AlbumForm
    context_object_name = 'album'

    def get_success_url(self):
        return reverse('photo:view', kwargs={'pk': self.object.pk})


class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = 'album/create.html'
    model = Album
    form_class = AlbumForm

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author_album = self.request.user
        album.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photos:album_view', kwargs={'pk': self.object.pk})

