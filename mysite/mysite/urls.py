from django.contrib import admin
from django.urls import path, include
from register import views as v
#These are the main URL paths, one for the administration, and the other linking to the main.urls file for furthing handling.

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
]
