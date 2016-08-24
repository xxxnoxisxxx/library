from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
	return render(request,'index.html', {})
	
@login_required
def opcja1(request):
	
	return render(request,'opcja1.html', {})
