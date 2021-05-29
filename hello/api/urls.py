from django.urls import include, path
from rest_framework import routers
from api.serializers import CommentsSet
from rest_framework.authtoken import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'comment', CommentsSet)


urlpatterns = [
    path('', include(router.urls)),]