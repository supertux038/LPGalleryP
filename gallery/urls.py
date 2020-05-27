from django.urls import path, re_path

from gallery import views
from gallery.views import ModelDelete

namespace = 'gallery'

urlpatterns = [
    path('', views.main, name='main'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('model/<int:num>', views.model, name='model'),
    path('userPage/', views.user_page, name='user_page'),
    re_path(r'^userPage/(?P<username>[0-9a-zA-Z\-_]+)', views.user_page, name='user_page'),
    path('<username>/addModel', views.AddModelView.as_view(), name='add_model'),
    # path('/removeModel/<int:model_id>', views.remove_model, name='remove_model'),
    re_path(r'^removeModel/(?P<pk>[0-9]+)', ModelDelete.as_view(), name='remove_model'),
    path('communities/', views.communities, name='communities'),
    path('models/', views.models, name='models'),
    re_path(r'models/(?P<param>[a-zA-Z]+)/(?P<argument>[а-яА-Я]+)', views.models, name='models'),
    path('userPage/<username>', views.user_page, name='my_user_page'),
    path('editProfile', views.edit_profile, name='edit_profile'),
    path('addComment', views.add_comment, name='add_comment'),
    path('404', views.page_not_found_test),
    path('500', views.internal_server_error_test)
]
