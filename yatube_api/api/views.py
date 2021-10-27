from django.contrib.auth.models import User
from rest_framework import filters, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Group, Post

from .permissions import AuthorPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permissions_class = (AuthorPermission, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorPermission, )

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all()
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        post_id = self.kwargs['post_id']
        get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user_id = self.request.user.pk
        user = get_object_or_404(User, id=user_id)
        follows = user.follower.all()
        return follows

    def perform_create(self, serializer):
        user_id = self.request.user.pk
        get_object_or_404(User, id=user_id)
        serializer.save(user=self.request.user)
