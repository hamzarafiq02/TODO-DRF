from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name="api-overview"),
    path('task-list/', views.Tasklist, name="task-list"),
    path('task-detail/<str:pk>', views.Taskdetail, name="task-detail"),
    path('task-create/', views.Taskcreate, name="task-create"),
    path('task-update/<str:pk>', views.Taskupdate, name="task-update"),
    path('task-delete/<str:pk>', views.Taskdelete, name="task-delete"),
]