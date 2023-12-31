from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = DefaultRouter()

router.register("studentapi",views.StudentModelViewset, basename="student")

urlpatterns = [
    path("admin/",admin.site.urls),
    path("",include(router.urls)),
    path("gettokens/",TokenObtainPairView.as_view(),name = "token_obtain_pair"),
    path("refresh/",TokenRefreshView.as_view(),name = "token_refresh"),
    path("verify/",TokenVerifyView.as_view(),name="token_verify")

]
