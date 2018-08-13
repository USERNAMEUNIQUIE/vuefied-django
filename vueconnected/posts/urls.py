from django.urls import  path ,include
from . import  views
from rest_framework.routers import  DefaultRouter


router =DefaultRouter()

router.register('postlist',views.PostList, base_name='PostList' )



urlpatterns = [

    path('',include(router.urls))
]
