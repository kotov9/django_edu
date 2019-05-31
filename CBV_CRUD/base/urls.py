from django.urls import path, re_path
from . import views

app_name = 'base'

urlpatterns = [
	re_path(r"injected_index/", views.IndexView.as_view(), name='index'),
	path('', views.SchoolIndexView.as_view(), name='home'),
	path('list/', views.SchoolListView.as_view(), name='list'),
	re_path(r'^list/(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
	re_path(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
	re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
	re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]