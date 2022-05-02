from django.contrib import admin
from django.urls import path
from manage import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('admin_user/hall_detail/<pk>/',views.hall_details_2,name='hall_detail'),
    path('admin_user/delete_hall/<str:pk>/',views.delete_hall,name='delete_hall'),
    path('admin_user/delete_lab/<str:pk>/',views.delete_lab,name='delete_lab'),
    path('admin_user/delete_day/<hall_id>/<str:pk>/',views.delete_day,name='delete_day'),
    path('admin_user/delete_day_lab/<lab_id>/<str:pk>/',views.delete_day_lab,name='delete_day_lab'),
    
    
    

    path('admin_user/convert_to_pdf/<pk>/',views.convert_to_pdf,name='convert_to_pdf'),
    path('admin_user/convert_to_pdf_lab/<pk>/',views.convert_to_pdf_lab,name='convert_to_pdf_lab'),
    

    path('admin_user/lab_detail/<pk>/',views.lab_details,name='lab_details'),
    path('admin_user/edit_day/<hall_id>/<pk>/',views.edit_day,name='edit_day'),
    path('admin_user/edit_day_in_lab/<lab_id>/<pk>/',views.edit_day_in_lab,name='edit_day_in_lab'),

    



    path('adminclick', views.adminclick_view),
    path('adminsignup', views.admin_signup_view), 
    path('adminlogin', LoginView.as_view(template_name='manage/adminlogin.html'),name="adminlogin"),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='manage/index.html'),name='logout'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-halls', views.admin_hall_view,name='admin-hall'),
    path('admin-lab', views.admin_lab_view,name='admin-lab'),
    path('admin-view-labs', views.admin_view_lab_view,name='admin-view-labs'),
    path('admin-view-hall', views.admin_view_hall_view,name='admin-view-hall'),


]






