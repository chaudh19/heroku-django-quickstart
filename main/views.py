from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from django.template import loader


from zxcvbn import zxcvbn

def index(request):
	return render(request, 'main/index.html', { })

def lookup(request):
	response_data = {}

	if request.POST.get('action') == 'post':
		word = request.POST.get('word')
	results = zxcvbn(word, user_inputs=[])

	response_data['score'] = results['score']
	response_data['crack_times_display'] = results['crack_times_display']
	return JsonResponse(response_data)

def wireframe1(request):
	arr = [1,1,1,1,1,1];
	return render(request, 'main/wireframe1.html', { "len":arr })

def wireframe2(request):
	# arr = [1,1,1,1,1,1];
	return render(request, 'main/wireframe2.html', { })
