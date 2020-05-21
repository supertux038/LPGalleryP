from django.contrib import admin
from django.urls import path, include

from gallery import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_func, name='logout'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('model/id<int:num>', views.model, name='model'),
    path('userPage/<username>', views.user_page, name='user_page'),
    path('addModel/', views.AddModelView.as_view(), name='add_model'),
    path('communities/', views.communities, name='communities'),
    path('404', views.page_not_found),
    path('500', views.internal_server_error)
]
