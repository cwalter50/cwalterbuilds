from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'ordersorter'

urlpatterns = [
    # ex: /ordersorter/
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("edit/<int:question_id>", views.edit, name="edit"),
    path('<int:question_id>/poll', views.poll, name='poll'),
    path('<int:question_id>/results', views.results, name='results'),


]

    
