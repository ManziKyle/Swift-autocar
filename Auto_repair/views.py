from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'home.html',{})



def about(request):
	return render(request,'about.html',{})



def locations(request):
	if request == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		Message = request.POST['Message']
		return render(request,'locations.html',{
			'name': name,
			'email': email,
			'phone': phone,
			'Message': Message
})

	else:
		return render(request,'locations.html',{})


def maintenance(request):
	return render(request,'maintenance.html',{})


def price(request):
	return render(request,'price.html',{})



def repair(request):
	return render(request,'repair.html',{})


def repair_info(request):
	return render(request,'repair_info.html',{})