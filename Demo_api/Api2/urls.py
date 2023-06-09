

from django.urls import path,include
from . import views
# from Api2.views import StudentViewSet
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'stu',StudentViewSet)
 
urlpatterns = [
    # path('generic-stulist/',Studentgeneric.as_view()),
    # path('generic-stulist/<id>',StudentGeneric1.as_view()),
    path('',views.ApiOverview,name='home'),
    path('create-data',views.list),
    path('create',views.add_student,name='add'),
    path('list/',views.stu_list,name='iist'),
    path('detail/<int:pk>/',views.detail_info,name='detail'),
    path('update/<int:pk>/',views.edit_list,name='update'),
    path('delete/<int:pk>/',views.delete_stu,name='delete'),
    path('show-data',views.show_data,name='show-data'),
    path('data-update/<int:pk>/',views.data_update,name='data-update'),
    path('data-delete/<int:pk>/',views.data_delete,name='data-delete')
]