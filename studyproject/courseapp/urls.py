from django.urls import path
from courseapp import views

app_name = 'courseapp'

urlpatterns=[
	path('',views.index,name='index'),
	

]