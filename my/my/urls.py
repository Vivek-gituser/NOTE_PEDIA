"""
URL configuration for my project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import viewss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',viewss.dashbord),
    path('digital_electronics',viewss.de),
    path('maths',viewss.maths),
    path('dsa',viewss.dsa),
    path('python',viewss.python),
    path('dstl',viewss.dstl),
    path('coa',viewss.coa),
    path('hv',viewss.hv),

    path('course',viewss.course),
    path('notes/', viewss.notes, name='resource'),
    path('pyq/<int:id>/',viewss.pyq),
    path('dpp/<int:id>/',viewss.dpp),
    path('questions/<int:id>/',viewss.questions)
]
