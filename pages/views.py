from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args , **kwargs):
	my_context = {
	   "my_text"      : "his is about us",
	   "my_number"    : 312,
	   "my_list"      : ["hardwork","Discipline","The bigger picture","Not giving up","God most of all",312,"abc"],
	   "this_is_true" : True,
	   "appreciation" : "We killing it"
	}
	return render(request,"home.html",my_context)


def contact_view(request,*args , **kwargs):
	return render(request,"contact.html",{})

