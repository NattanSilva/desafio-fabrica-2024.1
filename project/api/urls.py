from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import CharacterViewset

router = DefaultRouter()
router.register('characters', CharacterViewset)

urlpatterns = [
  path('api/',include(router.urls))
]