from django.urls import path
from webapp.views import (
    PhotoIndexView, PhotoUpdateView, PhotoView, PhotoDeleteView, PhotoCreateView,
    AlbumCreateView,
    AlbumDeleteView,
    AlbumUpdateView,
    AlbumView, PhotoCommentCreate,

)

app_name = 'photo'

urlpatterns = [

    path('', PhotoIndexView.as_view(), name='photo_list'),

    path('<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),

    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('album/', AlbumCreateView.as_view(), name='add'),
    path('album/<int:pk>/', AlbumView.as_view(), name='view'),
    path('<int:pk>/album/update/', AlbumUpdateView.as_view(), name='update'),
    path('<int:pk>/album/delete/', AlbumDeleteView.as_view(), name='delete'),

    path('<int:pk>/comments/add/', PhotoCommentCreate.as_view(), name='comment_create'),

]
