from django.shortcuts import render
from django.views.generic import (View, TemplateView, #Renders a given template, with the context containing parameters captured in the URL.
										DetailView,   # While this view is executing, self.object will contain the object that the view is operating upon.
										ListView,     # A page representing a list of objects.
												      # While this view is executing, self.object_list will contain the list of objects (usually, but not necessarily a queryset) that the view is operating upon.
										CreateView,
										UpdateView,
										DeleteView,)
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models

# Create your views here.
class IndexView(TemplateView):
	template_name = 'base/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['injected'] = 'works!'
		return context


class SchoolIndexView(TemplateView):
	# template_name = 'base/school_index.html'
	template_name = 'base/index.html'


class SchoolListView(ListView):
	model = models.School
	template_name = 'base/school_list.html'


class SchoolDetailView(DetailView):
	model = models.School
	context_object_name = 'school_detail'
	template_name = 'base/school_detail.html'


class SchoolCreateView(CreateView):
	model = models.School
	fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
	fields = ('name', 'principal')
	model = models.School
		

class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy('base:list')