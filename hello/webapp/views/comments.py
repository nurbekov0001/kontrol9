from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import Comment, Photo, Intermediate_table_of_cometaries_and_users


class PhotoCommentCreate(PermissionRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    form_class = CommentForm
    model = Comment
    permission_required = 'webapp.add_comment'

    def get_success_url(self):
        return reverse('photo:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        photo = get_object_or_404(Photo, id=self.kwargs.get('pk'))

        comment = form.instance
        comment.photo = photo
        comment.author = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Intermediate_table_of_cometaries_and_users.objects.filter(user=self.request.user)
        return context

