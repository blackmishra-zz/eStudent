from django.contrib import admin
from .models import EnrolledCourse, Ouser, User, Course, WishlistModel


admin.site.register(User)
admin.site.register(Ouser)
admin.site.register(Course)
admin.site.register(WishlistModel)
admin.site.register(EnrolledCourse)
