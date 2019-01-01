from . import views
from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('users/picture/<int:pk>', views.FileUploadView.as_view()),
    path('auth/login', views.AuthLogin.as_view()),
    path('auth/register', views.AuthRegister.as_view()),
]