"""
URL configuration for DjangoAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from api.login.login_view import login_views # Asegúrate de que estas importaciones son correctas
from api.home.home_view import home_views

urlpatterns = [
    # path('admin/', admin.site.urls),  # Ruta opcional para el panel de administración de Django
    path('', login_views, name='root'),  # Ruta vacía para la raíz, redirige a login_view
    path('login/', login_views, name='login_vista'),  # Ruta para login
    path('home/', home_views, name='home'),  # Ruta para la vista de home
]
