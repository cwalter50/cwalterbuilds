"""cwalterbuilds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# from django.conf.urls.static import static
# from django.conf import settings




# These are used for custom error pages...

handler404 = 'myprojects.views.error_404'
handler500 = 'myprojects.views.error_500'
handler403 = 'myprojects.views.error_403'
handler400 = 'myprojects.views.error_400'


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myprojects.urls")),
    path("polls/", include("polls.urls")),
    path("ordersorter/", include('ordersorter.urls'))
]

# if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


# this is added so that I do not have to call python3 manage.py collectstatic with every change to css files.
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]






