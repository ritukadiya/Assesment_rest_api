from django.contrib import admin
from django.urls import path
from myapp.views import TaskList,TaskDetail

urlpatterns = [
    path('api/Tasks',TaskList.as_view()),
    path('api/Tasks/<int:pk>',TaskDetail.as_view()),
    path('admin/', admin.site.urls),
]

