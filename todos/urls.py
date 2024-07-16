from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet,  basename='tasks')
router.register('todousers', views.ToDoUserViewSet, basename='todousers')

urlpatterns = router.urls