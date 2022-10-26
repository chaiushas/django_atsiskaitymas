from django.urls import path
from . import views
# . means from the same directory

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project'),
    path('register/', views.register, name='register'),
    path('myprojects/', views.MyProjectListView.as_view(), name='my-projects'),
]
