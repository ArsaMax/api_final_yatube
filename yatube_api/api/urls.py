from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewset, GroupViewSet, PostViewSet, FollowViewset

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewset)
router.register('follow', FollowViewset)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
