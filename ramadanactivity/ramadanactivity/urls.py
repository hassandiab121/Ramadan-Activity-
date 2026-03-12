"""
URL configuration for ramadanactivity project.

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
from django.urls import path, include
from django.conf.urls import handler404

import os
from recieveActivities.views import recieve_activities
from showActivities.views import custom_404_error

admin_url = os.getenv('AdminUrl','admin/')
handler404 = custom_404_error

urlpatterns = [
    path(admin_url, admin.site.urls),
    path('recieveactivity', recieve_activities, name='recieve_activities'),
    path('', include('showActivities.urls')),
]
