from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import User, Course, WishlistModel, EnrolledCourse


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class WishlistSerializers(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = WishlistModel
        fields = "__all__"


class EnrolledCourseSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = EnrolledCourse
        fields = "__all__"
