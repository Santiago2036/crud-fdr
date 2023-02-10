from rest_framework import routers
from .views import viewSetcomentario
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()

router.register('api/projects' , viewSetcomentario , 'projects' )

urlpatterns = router.urls