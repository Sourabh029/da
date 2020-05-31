
from django.urls import path
from . import views 
urlpatterns = [
   
    path('',views.index,name='index'),
    path('add',views.adddivs, name='add'),
    path('complete/<divs_id>', views.completeDivs,name='complete'),
    path('deletecomplete',views.deletecompleted ,name='deletecomplete'),
    path('deleteall',views.deleteAll,name='deleteall')


]