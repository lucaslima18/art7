from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import render

from utils.imdb import BestMovies, Search


class AboutTemplateView(TemplateView):
    template_name = 'index.html'

class HomeListView(ListView):
    context_object_name = "objeto"
    template_name = 'home.html'
    queryset = BestMovies()

    def search(self):
        search_text = self.POST.get("nome")
        content = Search(search_text)
        #import pdb
        #pdb.set_trace()
        return render(self ,'search.html', {"content": content})

    def get_context_data(self):
        context = super(HomeListView, self).get_context_data()
        context = {
            "soon_list": context["object_list"].soon_results,
            "critic_list": context["object_list"].critic_results,
            "public_list": context["object_list"].public_results,
            "trendings_list": context["object_list"].trendings_results

        }
        return context



class TesteTemplateView(TemplateView):
    template_name = 'bootstrap.html'
