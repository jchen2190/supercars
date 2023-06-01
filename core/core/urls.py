"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from supercars.views import get_homepage
from supercars.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", get_homepage, name="homepage"),
    path("supercars/", PostListView.as_view(), name="posts-all"),
    path("supercars/<int:pk>", PostDetailView.as_view(), name="posts-detail"),
    path("supercars/create/", PostCreateView.as_view(), name="posts-create"),
    path("supercars/update/<int:pk>/", PostUpdateView.as_view(), name="posts-update"),
    path("supercars/delete/<int:pk>/", PostDeleteView.as_view(), name="posts-delete"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)