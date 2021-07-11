from django.urls import path
from django.conf.urls import re_path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    re_path(r"^profile/$", views.profile, name="profile"),
    re_path(r"^profile/update/$", views.profile_update, name="profile_update"),
    path("courselist/", views.CourseList.as_view(), name="courselist"),
    path("courseoptions/<int:username>", views.CourseOptions.as_view()),
    path("enrolledcourse/", views.EnrolledCourseList.as_view()),
    path(
        "enrolledcourseoptions/<int:encourse_id>",
        views.EnrolledCourseListOptions.as_view(),
    ),
    path("wishlist/", views.WishList.as_view()),
    path("wishlistoptions/<int:wish_id>/", views.WishListOptions.as_view()),
]
