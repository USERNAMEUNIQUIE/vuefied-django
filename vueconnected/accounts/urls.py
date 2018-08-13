from django.urls import  path ,include
from . import  views
from rest_framework.routers import  DefaultRouter


router =DefaultRouter()

router.register('account',views.Userprofileviewsset )



urlpatterns = [
    path('login/', views.Loginviewset.as_view()),

    path('',include(router.urls))
]
