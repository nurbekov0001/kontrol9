from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers.comments import CommentSerializer
from webapp.models import Comment


class Article(APIView):
    def get(self, request, *args, **kwargs):
        try:
            article = Article.objects.get(pk=kwargs.get("pk"))
            article_srlz = CommentSerializer(article)
            response_data = article_srlz.data
            return Response(response_data)
        except Article.DoesNotExist:
            return Response(data={"error": "error"}, status=404)

    def put(self, request, pk, *args, **kwargs):
        try:
            article = Comment.objects.get(pk=pk)
            data = request.data
            update = CommentSerializer(instance=article, data=data)
            if update.is_valid(raise_exception=True):
                update.save()
            return Response(data=update.data)
        except Comment.DoesNotExist:
            return Response(data={"error": "error"}, status=404)

    def delete(self, request, pk, *args, **kwargs):
        try:
            article = Comment.objects.get(pk=pk)
            article.delete()
            return Response()
        except Comment.DoesNotExist:
            return Response(data={"error": "error"}, status=404)