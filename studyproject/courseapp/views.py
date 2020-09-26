from django.shortcuts import render
import json
import requests



# Create your views here.
def index(request):
	course_api_url= "https://staging.edulytx.com/api/courses/v1/courses"
	course_api_data=requests.get(course_api_url)
	print(course_api_data)
	return render(request,'index.html' )



