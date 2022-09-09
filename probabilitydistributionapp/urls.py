"""probabilitydistributionapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path
from distributions import views as distviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", distviews.home, name="home"),
    path("probdists/", distviews.index, name="home"),
    path("probdists/create_dist/", distviews.create_page),
    path("probdists/<id>/", distviews.probdist),
    path("probdists/<id>/update/", distviews.update_probdist),
    path("probdists/<id>/delete/", distviews.delete_probdist),
    path("probdists/<id>/create_normdist/", distviews.create_normdist),
    path("probdists/<id>/<dist_id>/update/", distviews.update_normdist),
    path("probdists/<id>/<dist_id>/delete/", distviews.delete_normdist),
]
