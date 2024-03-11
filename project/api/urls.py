from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import CharactersCreateView, CharactersListView
from .viewsets import CharacterViewset

router = DefaultRouter()
router.register('characters', CharacterViewset)

urlpatterns = [
  path('api/',include(router.urls)),
  path('', CharactersCreateView.as_view(), name="home"),
  path('list/', CharactersListView.as_view(), name="characters_list")
]