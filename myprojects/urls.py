from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from django.conf.urls import include


from . import views

app_name = 'myprojects'

urlpatterns = [
    path("", views.index, name="index"),
    path("myprojects", views.myprojects, name="myprojects"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    # path('accounts/', include('django.contrib.auth.urls')),
    
]