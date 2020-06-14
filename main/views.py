from django.http import HttpResponse
from zxcvbn import zxcvbn

def index(request):
	results = zxcvbn('JohnSmith123', user_inputs=['John', 'Smith'])
	print(results)
	# https://github.com/dwolfhub/zxcvbn-python
	return HttpResponse("Hello, world. You're at the main index.")