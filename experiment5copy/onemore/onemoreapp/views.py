from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from onemoreapp.forms import EmployeeForm
from onemoreapp.models import Person



def ppl(request):
	if request.method == "POST":
		if request.POST['name'] and request.POST['image']:
			post = Person()
			post.first_name = request.POST['name']
			post.last_name = request.POST['image']
			print(post.first_name)
			post.save()
			user = authenticate(request, username=post.first_name,password=post.last_name)
			if user:
				login(request, user)
				return HttpResponseRedirect(reverse('user_success'))
			else:
				return render(request,"index.html")
	else:
		return render(request,"index.html")







def user_login(request):
	context={}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		print(password)
		user = authenticate(request, username=username,password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('user_success'))
		else:
			context["error"] = "text error"
			return render(request,"login.html",context)
	else:
		return render(request,"login.html",context)


def show(request):
	people = Person.objects.all()
	return render(request,"show.html",{'ppl':people})



def allconnected(request):
	if request.method == "POST":
		if request.POST['userconnected'] and request.POST['passwordconnected']:
			post = Person()
			post.first_name = request.POST['userconnected']
			post.last_name = request.POST['passwordconnected']
			post.save()
			user = authenticate(request, username=post.first_name,password=post.last_name)
			if user:
				login(request, user)
				return HttpResponseRedirect(reverse('user_success'))
			else:
				return render(request,"signin.html")
	else:
		return render(request,"signin.html")

