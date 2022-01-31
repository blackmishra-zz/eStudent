from django.http import request
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from rest_framework import generics, permissions
from .serializers import (
    userSerializers,
    CourseSerializers,
    WishlistSerializers,
    EnrolledCourseSerializer,
)
from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
from .models import User, WishlistModel, Course, EnrolledCourse


def login(request):
    return render(request, "accounts/login")


def logout(request):
    return render(request, "accounts/logout")


@login_required
def profile(request):
    user = request.user
    request.session["username"] = user.username
    return render(request, "account/profile.html", {"user": user})


class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializers

    def get_queryset(self):

        return Course.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class EnrolledCourseList(generics.ListCreateAPIView):
    serializer_class = EnrolledCourseSerializer

    def get_queryset(self):
        username = self.request.session["username"]
        return EnrolledCourse.objects.filter(username=username)

    def perform_create(self, serializer):
        username = self.request.session["username"]
        serializer.save(username=username)


class EnrolledCourseListOptions(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EnrolledCourseSerializer
    lookup_url_kwarg = "encourse_id"

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        return EnrolledCourse.objects.filter(id=id)


class CourseOptions(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializers
    lookup_url_kwarg = "username"
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        return Course.objects.filter(id=id)


class WishList(generics.ListCreateAPIView):
    serializer_class = WishlistSerializers

    def get_queryset(self):
        username = self.request.session["username"]
        return WishlistModel.objects.filter(username=username)

    def perform_create(self, serializer):
        username = self.request.session["username"]
        serializer.save(username=username)


class WishListOptions(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishlistSerializers
    lookup_url_kwarg = "wish_id"

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        return WishlistModel.objects.filter(id=id)
    

class ZoomUrlRedirect(APIView):
    """Receives User access token after successful zoom authentication."""

    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        access_token = request.data.get("access_token")
        print(access_token)
        return Response(access_token, status=status.HTTP_200_OK)
