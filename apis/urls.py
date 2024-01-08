from django.urls import path
from .views import ToDoViewSet
from rest_framework.routers import DefaultRouter

# from .views import ListTodo, DetailTodo   # This is for view

# This url is for view.
'''urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]'''

router = DefaultRouter()
router.register('', ToDoViewSet, basename='ToDo')
urlpatterns = router.urls