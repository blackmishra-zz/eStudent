from django.urls import path
from django.conf.urls import re_path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    re_path(r"^profile/$", views.profile, name="profile"),
    path("courselist/", login_required(views.CourseList.as_view()), name="courselist"),
    path("courseoptions/<int:username>", login_required(views.CourseOptions.as_view())),
    path("enrolledcourse/", login_required(views.EnrolledCourseList.as_view())),
    path(
        "enrolledcourseoptions/<int:encourse_id>",
        login_required(views.EnrolledCourseListOptions.as_view()),
    ),
    path("wishlist/", login_required(views.WishList.as_view())),
    path("zoom/callback/", views.ZoomUrlRedirect.as_view(),
    path(
        "wishlistoptions/<int:wish_id>/",
        login_required(views.WishListOptions.as_view()),
    ),
]
