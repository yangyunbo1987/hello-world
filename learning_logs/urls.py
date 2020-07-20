"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views

# app_name='learning_logs'
# urlpatterns = [
#     # Home page.
#     path(r'', views.index, name='index'),
#
#     # Show all topics.
#     path(r'topics/', views.topics, name='topics'),
#
#     # Detail page for a single topic.
#     #path('topic/<int:topic_id>/', views.topic, name='topic'),
# ]
app_name = 'learning_logs'
urlpatterns = [
    #主页
    path(r'', views.index, name='index'),
    #显示所有主题页面
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]#注意是中括号，不是大括号，这块出错花了我很长时间。。。