from django.urls import path
from . import views
app_name='todo_app'
urlpatterns=[
    path('',views.home,name='home'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('cbv_home/',views.TaskListView.as_view(),name="cbv_home"),
    path('cbv_detail/<int:pk>/',views.TaskDetailView.as_view(),name="cbv_detail"),
    path('cbv_update/<int:pk>/',views.TaskUpdateView.as_view(),name="cbv_update"),
    path('cbv_delete/<int:pk>/',views.TaskDeleteView.as_view(),name="cbv_delete"),

]