from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('data-entry/',views.createData, name = 'create'),
    path('newproduct/',views.createProduct, name = 'createP'),
    path('delete/<str:pk>/',views.deleteData, name = 'delete-entry'),
    path('deleteall',views.deleteAll, name = 'deleteAll-entry'),
    path('edit/<str:pk>/',views.editData, name = 'edit-entry'),
    
]
