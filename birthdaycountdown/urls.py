from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from django.conf.urls import include


from . import views

app_name = 'birthdaycountdown'

urlpatterns = [
    path("", views.index, name="index")
]