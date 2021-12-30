from django.shortcuts import render




def nodb(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		print(password)
		return render(request,"index.html")