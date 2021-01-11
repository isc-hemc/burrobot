"""Context urls module."""

from django.urls import path

from ..context.views import ContextDetail, ContextList

urlpatterns = [
    path("", ContextList.as_view(), name="context-list"),
    path("<int:pk>/", ContextDetail.as_view(), name="context-detail"),
]
