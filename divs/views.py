from django.shortcuts import render,redirect


from django.views.decorators.http import require_POST
from .models import divs
from .forms import divsForm
# Create your views here.
def index(request):
	divs_list=divs.objects.order_by('id')

	form=divsForm()

	context={'divs_list': divs_list, 'form' : form}
	return render(request,'divs/index.html', context)
@require_POST
def adddivs(request):
		form=(request.POST['text'])
		creat_obj=divs.objects.create(text=form)

		

		return redirect('index')
def completeDivs(request,divs_id):
	Divs= divs.objects.get(pk=divs_id)
	Divs.complete=True
	Divs.save()

	return redirect('index')
def deletecompleted(request):
	divs.objects.filter(complete__exact=True).delete()

	return redirect('index')
def deleteAll(request):
	divs.objects.all().delete()
	return redirect('index')
