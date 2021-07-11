from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

import users


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="users/index.html")),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include(("users.urls", "users"), namespace="accounts")),
    path("users/", include("users.urls")),
    path("logout/", LogoutView.as_view()),
    # path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
