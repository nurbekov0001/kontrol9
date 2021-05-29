from rest_framework import serializers

from webapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_photo', 'comment', 'author', 'created_at')
        read_only_fields = ('author', 'id', "created_at")
