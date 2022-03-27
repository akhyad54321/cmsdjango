from django.contrib import admin
from django.urls import path
from cms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.addCompany, name='createtodo'),
    path('listcompany/', views.listCompany, name='myCompany'),
    path('myCompany/<int:edit_pk>', views.edit, name='edit'),
    path('myCompany/<int:company_pk>/delete', views.deletecompany, name='deletecompany'),
]
