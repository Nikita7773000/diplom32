from django.contrib.auth.views import LoginView

from . import views
from django.urls import path

urlpatterns = [path('', views.main,name='main'),
               path('list/', views.my_view, name="list-book"),
               path('grade', views.grade, name='grade'),
               path('author', views.author, name='author'),
               path('grade_list', views.grade_list, name='grade_list'),
               path('registr/', views.registr, name='registr'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('<int:pk>', views.MyDetailView1.as_view(), name='mydetail'),
               ]
