from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_activities, name='show_activities'),
    path('<int:id>/', views.activity_detail, name='activity_detail'),
    path('<int:id>/join/', views.join_activity, name='join_activity'),
    path('by-date/', views.activities_by_date_json, name='activities_by_date_json'),
]
