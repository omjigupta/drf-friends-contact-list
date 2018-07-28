from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^friends/(?P<pk>[0-9]+)$',
        views.get_delete_update_friend,
        name='get_delete_update_friend'
    ),
    url(
        r'^friends/$',
        views.get_post_friends,
        name='get_post_friends'
    )
]
