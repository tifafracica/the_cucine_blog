"""Myfirstmvt URL Configuration

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

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Posts import views

urlpatterns = [
    path('', views.ShowHomePage, name='Home'),
    path('about', views.ShowAboutPage, name='About Page'),
    path('search_page/', views.findPage, name='Search Page'),
    path('get_pages/', views.PostList.as_view(), name='List Posts'),
    path("create_page/", views.PostCreation.as_view(), name="Create Post"),
    path("get_page/<pk>", views.PostDetail.as_view(), name="Get Post"),
    path("update_page/<pk>", views.PostUpdate.as_view(), name='Update Post'),
    path("post_confirm_delete/<pk>", views.PostDelete.as_view(), name='Delete Post'),
    path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('accounts/login/', views.AdminLoginView.as_view(), name='Login'),
    path('accounts/logout/', views.AdminLogoutView.as_view(), name='Logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)