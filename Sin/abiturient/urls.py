from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('header',HeadisView)

urlpatterns = [
    path('head/',HeadView.as_view()),
    path('',include(router.urls))

]
