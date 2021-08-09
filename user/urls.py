from django.urls import path, re_path
from user import views


app_name = 'user'

urlpatterns = [
    path('regist/', views.regist, name='regist'),
    path('regist/<user_id>', views.regist_2, name='regist2'),
]