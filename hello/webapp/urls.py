from django.urls import path
from webapp.views import (
    PhotoIndexView, PhotoUpdateView, PhotoView, PhotoDeleteView, PhotoCreateView,
    AlbumCreateView,
    AlbumDeleteView,
    AlbumUpdateView,
    AlbumView,
    AlbumIndexView
)

app_name = 'photo'

urlpatterns = [
    # path('tracers/', IndexView.as_view(), name='list'),
    # path('<int:pk>/', TracerView.as_view(), name='view'),
    # path('<int:pk>/update/', TracerUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', TracerDeleteView.as_view(), name='delete'),

    # path('user/<int:pk>', UserUpdateView.as_view(), name="user_update"),
    #
    # path('project_tracer/<int:pk>/add/', ProjectTracerCreate.as_view(), name='project_tracer_add'),

    path('', PhotoIndexView.as_view(), name='photo_list'),
    path('add/', PhotoCreateView.as_view(), name='photo_add'),
    path('<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),

    path('album/add/', AlbumCreateView.as_view(), name='add'),
    path('album/<int:pk>/', AlbumView.as_view(), name='view'),
    path('album/<int:pk>/update/', AlbumUpdateView.as_view(), name='update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='delete'),

]
