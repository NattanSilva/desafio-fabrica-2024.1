from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .api.viewsets import CharacterViewset
from .models import Character


class CharactersCreateView(CreateView):
  model = Character
  template_name = 'character/home.html'
  fields = ['name']
  success_url = reverse_lazy('characters_list')


  def post(self, request: HttpRequest, *args: str, **kwargs: reverse_lazy) -> HttpResponse:
    return super().post(request, *args, **kwargs)

class CharactersListView(ListView):
  model = Character
  template_name = 'character/list.html'
  queryset = Character.objects.all()