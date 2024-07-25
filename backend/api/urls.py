from django.urls import path
from . import views

urlpatterns = [
  path("media/", views.MediaListCreate.as_view(), name="media-list"),
  path("media/delete/<int:pk>/", views.MediaDelete.as_view(), name="delete-media"),
]